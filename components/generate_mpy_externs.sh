#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(cd "${script_dir}/.." && pwd)"

target="${TARGET:-esp32s3}"
case "${target}" in
    esp3-s3|esp32-s3)
        target="esp32s3"
        ;;
esac

build_dir="${BUILD_DIR:-${script_dir}/build-${target}}"
native_obj="${NATIVE_OBJ:-${build_dir}/ROSMicroPy.normalized.o}"
firmware_elf="${FIRMWARE_ELF:-${repo_dir}/micropython/ports/esp32/build/micropython.elf}"
output="${1:-${build_dir}/firmware_externs.ld}"

case "${target}" in
    esp32s3)
        nm_tool="${NM:-xtensa-esp32s3-elf-nm}"
        ;;
    esp32s2)
        nm_tool="${NM:-xtensa-esp32s2-elf-nm}"
        ;;
    esp32)
        nm_tool="${NM:-xtensa-esp32-elf-nm}"
        ;;
    *)
        nm_tool="${NM:-nm}"
        ;;
esac

if [[ ! -f "${native_obj}" ]]; then
    printf 'Native object not found: %s\n' "${native_obj}" >&2
    exit 1
fi

if [[ ! -f "${firmware_elf}" ]]; then
    printf 'Firmware ELF not found: %s\n' "${firmware_elf}" >&2
    printf 'Build firmware first or set FIRMWARE_ELF=/path/to/micropython.elf\n' >&2
    exit 1
fi

tmp_undef="$(mktemp)"
tmp_defined="$(mktemp)"
trap 'rm -f "${tmp_undef}" "${tmp_defined}"' EXIT

"${nm_tool}" -u "${native_obj}" | awk '{print $2}' | sort -u > "${tmp_undef}"
"${nm_tool}" -g "${firmware_elf}" | awk 'NF >= 3 && $2 != "U" {print $1, $3}' | sort -k2,2 -u > "${tmp_defined}"

mkdir -p "$(dirname "${output}")"
awk '
    NR == FNR {
        needed[$1] = 1
        next
    }
    $2 in needed {
        printf "%s = 0x%s;\n", $2, $1
        resolved[$2] = 1
    }
    END {
        for (symbol in needed) {
            if (!(symbol in resolved) && symbol != "mp_native_qstr_table") {
                missing = 1
                printf "missing extern: %s\n", symbol > "/dev/stderr"
            }
        }
        exit missing ? 1 : 0
    }
' "${tmp_undef}" "${tmp_defined}" > "${output}"

printf 'Wrote %s\n' "${output}"
