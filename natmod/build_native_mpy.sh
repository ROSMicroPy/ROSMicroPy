#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(cd "${script_dir}/.." && pwd)"

target="${TARGET:-esp32s3}"

case "${target}" in
    esp3-s3|esp32-s3)
        target="esp32s3"
        ;;
    esp32s3|esp32s2|esp32)
        ;;
    x64|host)
        target="host"
        ;;
    *)
        printf 'Unsupported TARGET=%s\n' "${target}" >&2
        printf 'Supported targets: esp32s3, esp32s2, esp32, host\n' >&2
        exit 2
        ;;
esac

if [[ "${target}" == "host" ]]; then
    arch="${ARCH:-x64}"
else
    arch="${ARCH:-xtensawin}"
fi

build_dir="${BUILD_DIR:-${script_dir}/build-${target}}"
mpy_dir="${MPY_DIR:-${repo_dir}/micropython}"

cmake -S "${script_dir}" -B "${build_dir}" \
    -DMPY_DIR="${mpy_dir}" \
    -DMPY_ARCH="${arch}" \
    -DMPY_TARGET="${target}"

cmake --build "${build_dir}" --target native_mpy

printf 'Built %s\n' "${build_dir}/ROSMicroPy.mpy"
