import re


PRIMITIVES = {
    "bool", "byte", "char",
    "int8", "uint8", "int16", "uint16", "int32", "uint32", "int64", "uint64",
    "float32", "float64", "double", "string", "wstring",
}

ALIASES = {
    "boolean": "bool",
    "octet": "uint8",
    "float": "float32",
    "double": "float64",
    "wstring": "string",
}

TYPE_RE = re.compile(r"^(?P<base>[A-Za-z][A-Za-z0-9_/]*)(?:<=(?P<bound>\d+))?(?P<array>\[(?:(?P<array_bound><=)?(?P<array_len>\d+)?)?\])?$")


def make_component(spec):
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


def _strip_comment(line):
    in_quote = None
    for i, ch in enumerate(line):
        if ch in ("'", '"'):
            in_quote = None if in_quote == ch else ch
        elif ch == "#" and in_quote is None:
            return line[:i]
    return line


def _parse_value(text):
    text = text.strip()
    if text in ("true", "True"):
        return True
    if text in ("false", "False"):
        return False
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ("'", '"'):
        return text[1:-1]
    try:
        return int(text, 0)
    except Exception:
        pass
    try:
        return float(text)
    except Exception:
        return text


def _parse_type(type_text, package):
    match = TYPE_RE.match(type_text)
    if not match:
        raise ValueError("unsupported type syntax: %s" % type_text)

    base = match.group("base")
    base = ALIASES.get(base, base)
    if "/" in base:
        parts = base.split("/")
        if len(parts) == 2:
            _, type_name = parts
        elif len(parts) == 3:
            _, _, type_name = parts
        else:
            raise ValueError("unsupported qualified type: %s" % base)
    else:
        type_name = base

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

    return type_name, is_array, is_sequence, capacity


def _parse_idl_fields(contents, package):
    fields = []
    constants = []
    idl_lines = []
    for raw in contents.splitlines():
        line = _strip_comment(raw).strip()
        if not line:
            continue
        idl_lines.append(line)
        if "=" in line:
            left, value = line.split("=", 1)
            parts = left.split()
            if len(parts) >= 2:
                constants.append((parts[1], _parse_value(value)))
                continue
        parts = line.split(None, 2)
        if len(parts) < 2:
            continue
        type_name, is_array, is_sequence, capacity = _parse_type(parts[0], package)
        fields.append((parts[1], type_name, (), is_array, is_sequence, capacity))
    return tuple(fields), constants, idl_lines


def _default_for_field(field):
    _, type_name, children, is_array, is_sequence, _ = field
    if is_array or is_sequence:
        return []
    if children:
        return {}
    if type_name == "bool":
        return False
    if type_name == "string" or type_name == "wstring":
        return ""
    if type_name in ("float32", "float64", "double"):
        return 0.0
    return 0


def _create_message_class(name, namespace, fields, constants, idl_lines):
    field_types = {}
    attrs = {
        "_TYPE_NAME": name,
        "_TYPE_DEF": (name, namespace, fields),
        "_fields_and_field_types": field_types,
        "_IDL_LINES": tuple(idl_lines),
    }
    defaults = {}
    for field in fields:
        fname, type_name, _, is_array, is_sequence, capacity = field
        type_text = _field_type_to_idl(type_name, is_array, is_sequence, capacity)
        field_types[fname] = type_text
        defaults[fname] = _default_for_field(field)
    for const_name, const_value in constants:
        attrs[const_name] = const_value

    def __init__(self, *args, **kwargs):
        names = list(field_types)
        if len(args) > len(names):
            raise TypeError("expected at most %d arguments" % len(names))
        for i, value in enumerate(args):
            kwargs[names[i]] = value
        for fname in field_types:
            if fname in kwargs:
                value = kwargs.pop(fname)
            else:
                default = defaults[fname]
                value = [] if default == [] else default
            self[fname] = value
        if kwargs:
            raise TypeError("unexpected argument: %s" % next(iter(kwargs)))

    attrs["__init__"] = __init__
    return type(name, (Message,), attrs)


def _field_type_to_idl(type_name, is_array=False, is_sequence=False, capacity=0):
    if is_array:
        return "%s[%d]" % (type_name, capacity)
    if is_sequence:
        return "%s[<=%d]" % (type_name, capacity) if capacity else "%s[]" % type_name
    if capacity and (type_name == "string" or type_name == "wstring"):
        return "%s<=%d" % (type_name, capacity)
    return type_name


def _class_to_idl(data_type_class):
    if hasattr(data_type_class, "Request") and hasattr(data_type_class, "Response"):
        request = _class_to_idl(data_type_class.Request)
        response = _class_to_idl(data_type_class.Response)
        return request.rstrip() + "\n---\n" + response.lstrip()

    idl_lines = getattr(data_type_class, "_IDL_LINES", None)
    if idl_lines:
        return "\n".join(idl_lines) + "\n"

    type_def = getattr(data_type_class, "_TYPE_DEF", None)
    if type_def is None:
        raise ValueError("data_type_class must be a Message subclass or service class")
    lines = []
    for name, type_name, _, is_array, is_sequence, capacity in type_def[2]:
        lines.append("%s %s" % (_field_type_to_idl(type_name, is_array, is_sequence, capacity), name))
    return "\n".join(lines) + ("\n" if lines else "")


class Message:
    _TYPE_NAME = ''
    _TYPE_DEF = None
    _fields_and_field_types = {}

    def __getitem__(self, name):
        try:
            return getattr(self, name)
        except AttributeError:
            raise KeyError(name)

    def __setitem__(self, name, value):
        setattr(self, name, value)

    def __contains__(self, name):
        return name in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    @classmethod
    def get_fields_and_field_types(cls):
        return dict(cls._fields_and_field_types)

    @classmethod
    def get_data_map(cls):
        return make_data_map(cls._TYPE_DEF)

    @property
    def dataMap(self):
        return self.get_data_map()

    @classmethod
    def parse_IDL(cls, contents, type_name="ParsedMessage", package="rosmicropy", kind="msg"):
        if "---" in contents:
            request, response = contents.split("---", 1)
            service_name = type_name or "ParsedService"
            request_class = cls.parse_IDL(request, service_name + "_Request", package, "srv")
            response_class = cls.parse_IDL(response, service_name + "_Response", package, "srv")
            return type(service_name, (), {"Request": request_class, "Response": response_class})

        fields, constants, idl_lines = _parse_idl_fields(contents, package)
        namespace = "%s::%s" % (package, kind)
        return _create_message_class(type_name, namespace, fields, constants, idl_lines)

    @classmethod
    def parse_IDL_File(cls, filename, type_name=None, package=None, kind=None):
        with open(filename, "r") as infile:
            contents = infile.read()
        if type_name is None:
            stem = filename.replace("\\", "/").rsplit("/", 1)[-1].rsplit(".", 1)[0]
            type_name = stem or "ParsedMessage"
        if kind is None:
            suffix = filename.rsplit(".", 1)[-1] if "." in filename else "msg"
            kind = "srv" if suffix == "srv" else "msg"
        if package is None:
            package = "rosmicropy"
        return cls.parse_IDL(contents, type_name, package, kind)

    parse_IDLFile = parse_IDL_File

    @staticmethod
    def export_IDL(data_type_class, filename=None):
        contents = _class_to_idl(data_type_class)
        if filename is None:
            print(contents, end="")
        else:
            with open(filename, "w") as outfile:
                outfile.write(contents)
        return contents
