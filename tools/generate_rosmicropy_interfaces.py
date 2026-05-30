#!/usr/bin/env python3
import ast
import os
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "components/libROSMicroPy/py"

SOURCES = [
    ROOT / "ext_lib/common_interfaces",
    ROOT / "components/micro_ros_espidf_component/micro_ros_src/src/rcl_interfaces/action_msgs",
]

PRIMITIVES = {
    "bool", "byte", "char",
    "int8", "uint8", "int16", "uint16", "int32", "uint32", "int64", "uint64",
    "float32", "float64", "double", "string",
    "wstring",
}

ALIASES = {
    "boolean": "bool",
    "octet": "uint8",
    "float": "float32",
    "double": "float64",
}

TYPE_RE = re.compile(r"^(?P<base>[A-Za-z][A-Za-z0-9_/]*)(?:<=(?P<bound>\d+))?(?P<array>\[(?:(?P<array_bound><=)?(?P<array_len>\d+)?)?\])?$")


def snake(name):
    out = []
    for i, ch in enumerate(name):
        if ch.isupper() and i and (not name[i - 1].isupper() or (i + 1 < len(name) and name[i + 1].islower())):
            out.append("_")
        out.append(ch.lower())
    return "".join(out)


def strip_comment(line):
    in_quote = None
    for i, ch in enumerate(line):
        if ch in ("'", '"'):
            in_quote = None if in_quote == ch else ch
        elif ch == "#" and in_quote is None:
            return line[:i]
    return line


def parse_value(text):
    text = text.strip()
    if not text:
        return None
    if text in ("true", "True"):
        return True
    if text in ("false", "False"):
        return False
    try:
        return ast.literal_eval(text)
    except Exception:
        pass
    try:
        return int(text, 0)
    except Exception:
        pass
    try:
        return float(text)
    except Exception:
        return text


def parse_type(type_text, package):
    match = TYPE_RE.match(type_text)
    if not match:
        raise ValueError("unsupported type syntax: %s" % type_text)

    base = match.group("base")
    base = ALIASES.get(base, base)
    if "/" in base:
        parts = base.split("/")
        if len(parts) == 2:
            ref_pkg, ref_name = parts
        elif len(parts) == 3:
            ref_pkg, _, ref_name = parts
        else:
            raise ValueError("unsupported qualified type: %s" % base)
        type_name = ref_name
        ref = (ref_pkg, "msg", ref_name)
    elif base in PRIMITIVES:
        type_name = base
        ref = None
    else:
        type_name = base
        ref = (package, "msg", base)

    array_text = match.group("array")
    bound = match.group("bound")
    array_len = match.group("array_len")
    is_array = False
    is_sequence = False
    capacity = int(bound) if bound else 0

    if array_text is not None:
        if array_len and not match.group("array_bound"):
            is_array = True
            capacity = int(array_len)
        else:
            is_sequence = True
            capacity = int(array_len) if array_len else capacity

    return type_name, ref, is_array, is_sequence, capacity


def parse_msg(path, package, namespace_kind="msg"):
    fields = []
    constants = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = strip_comment(raw).strip()
        if not line:
            continue
        if "=" in line:
            left, value = line.split("=", 1)
            parts = left.split()
            if len(parts) >= 2:
                type_text, name = parts[0], parts[1]
                constants.append((name, parse_value(value)))
            continue
        parts = line.split(None, 2)
        if len(parts) < 2:
            continue
        type_name, ref, is_array, is_sequence, capacity = parse_type(parts[0], package)
        fields.append((parts[1], type_name, ref, is_array, is_sequence, capacity))
    return fields, constants


def discover():
    defs = {}
    for source in SOURCES:
        if not source.exists():
            continue
        roots = [source] if (source / "package.xml").exists() else [p for p in source.iterdir() if (p / "package.xml").exists()]
        for pkg_root in roots:
            package = pkg_root.name
            for kind in ("msg", "srv"):
                for path in sorted((pkg_root / kind).glob("*.%s" % kind)):
                    if kind == "msg":
                        fields, constants = parse_msg(path, package, "msg")
                        defs[(package, "msg", path.stem)] = (fields, constants)
                    else:
                        request, response = path.read_text(encoding="utf-8").split("---", 1)
                        req_tmp = OUT / "_tmp_request.srv"
                        resp_tmp = OUT / "_tmp_response.srv"
                        req_tmp.write_text(request, encoding="utf-8")
                        resp_tmp.write_text(response, encoding="utf-8")
                        try:
                            defs[(package, "srv", path.stem + "_Request")] = (*parse_msg(req_tmp, package, "srv"),)
                            defs[(package, "srv", path.stem + "_Response")] = (*parse_msg(resp_tmp, package, "srv"),)
                        finally:
                            req_tmp.unlink(missing_ok=True)
                            resp_tmp.unlink(missing_ok=True)
    return defs


def component_tuple(field, defs, seen):
    name, type_name, ref, is_array, is_sequence, capacity = field
    children = ()
    if ref and ref in defs:
        if ref in seen:
            children = ()
        else:
            children = tuple(component_tuple(child, defs, seen | {ref}) for child in defs[ref][0])
    return (name, type_name, children, is_array, is_sequence, capacity)


def default_for(field):
    _, type_name, ref, is_array, is_sequence, _ = field
    if is_array or is_sequence:
        return "[]"
    if ref:
        return "{}"
    if type_name == "bool":
        return "False"
    if type_name == "string" or type_name == "wstring":
        return "''"
    if type_name in ("float32", "float64", "double"):
        return "0.0"
    return "0"


def write_runtime():
    runtime = OUT / "rosmicropy_interfaces.py"
    runtime.write_text(
        """def make_component(spec):
    name, typ, children, is_array, is_sequence, cap = spec
    item = {'name': name, 'type': typ}
    if children:
        item['components'] = [make_component(child) for child in children]
    if is_array:
        item['isArray'] = True
    if is_sequence:
        item['isSequence'] = True
    if cap:
        item['capicity'] = cap
    return item

def make_data_map(type_def):
    name, namespace, fields = type_def
    return {'message_name': name, 'message_namespace': namespace, 'components': [make_component(field) for field in fields]}

class Message(dict):
    __slots__ = ()
    _TYPE_NAME = ''
    _TYPE_DEF = None
    _fields_and_field_types = {}

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value

    @classmethod
    def get_fields_and_field_types(cls):
        return dict(cls._fields_and_field_types)

    @classmethod
    def get_data_map(cls):
        return make_data_map(cls._TYPE_DEF)

    @property
    def dataMap(self):
        return self.get_data_map()
""",
        encoding="utf-8",
    )


def write_package(package, by_kind, defs):
    pkg_dir = OUT / package
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)
    pkg_dir.mkdir(parents=True)
    (pkg_dir / "__init__.py").write_text("", encoding="utf-8")

    for kind, entries in by_kind.items():
        kind_dir = pkg_dir / kind
        kind_dir.mkdir()
        imports = []
        type_lines = ["_TYPE_DEFS = {"]
        for name, fields, constants in entries:
            key = (package, kind, name)
            namespace = "%s::%s" % (package, kind)
            components = tuple(component_tuple(field, defs, {key}) for field in fields)
            type_lines.append("    %r: (%r, %r, %r)," % (name, name, namespace, components))
        type_lines.append("}")
        (kind_dir / "_types.py").write_text("\n".join(type_lines) + "\n", encoding="utf-8")

        for name, fields, constants in entries:
            field_types = {f[0]: f[1] for f in fields}
            lines = [
                "from rosmicropy_interfaces import Message",
                "from ._types import _TYPE_DEFS",
                "",
                "class %s(Message):" % name,
                "    _TYPE_NAME = %r" % name,
                "    _TYPE_DEF = _TYPE_DEFS[%r]" % name,
                "    _fields_and_field_types = %r" % field_types,
            ]
            for const_name, const_value in constants:
                lines.append("    %s = %r" % (const_name, const_value))
            args = ", ".join("%s=None" % f[0] for f in fields)
            lines.append("")
            lines.append("    def __init__(self, %s):" % args if args else "    def __init__(self):")
            if fields:
                for field in fields:
                    fname = field[0]
                    default = default_for(field)
                    lines.append("        self[%r] = %s if %s is None else %s" % (fname, default, fname, fname))
            else:
                lines.append("        pass")
            lines.append("")
            lines.append("dataMap = %s.get_data_map()" % name)
            (kind_dir / ("%s.py" % name)).write_text("\n".join(lines) + "\n", encoding="utf-8")
            imports.append("from .%s import %s" % (name, name))

        imports.append("__all__ = %r" % [entry[0] for entry in entries])
        (kind_dir / "__init__.py").write_text("\n".join(imports) + "\n", encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    defs = discover()
    write_runtime()

    grouped = {}
    for (package, kind, name), (fields, constants) in sorted(defs.items()):
        grouped.setdefault(package, {}).setdefault(kind, []).append((name, fields, constants))

    for package, by_kind in grouped.items():
        write_package(package, by_kind, defs)

    total = sum(len(entries) for by_kind in grouped.values() for entries in by_kind.values())
    print("generated %d interfaces in %s" % (total, OUT))


if __name__ == "__main__":
    main()
