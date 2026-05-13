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
microros_include_dir="${MICROROS_INCLUDE_DIR:-${script_dir}/micro_ros_espidf_component/include}"
microros_lib="${MICROROS_LIB:-${script_dir}/micro_ros_espidf_component/libmicroros.a}"
firmware_elf="${FIRMWARE_ELF:-${repo_dir}/micropython/ports/esp32/build/micropython.elf}"

cmake_args=(
    -DMPY_DIR="${mpy_dir}"
    -DMPY_ARCH="${arch}"
    -DMPY_TARGET="${target}"
    -DMICROROS_INCLUDE_DIR="${microros_include_dir}"
    -DMICROROS_LIB="${microros_lib}"
)

if [[ -n "${MPY_EXTERNS_FILE:-}" ]]; then
    cmake_args+=(-DMPY_EXTERNS_FILE="${MPY_EXTERNS_FILE}")
elif [[ "${target}" != "host" && -f "${firmware_elf}" ]]; then
    cmake -S "${script_dir}" -B "${build_dir}" \
        "${cmake_args[@]}" \
        -DMPY_EXTERNS_FILE:FILEPATH=

    cmake --build "${build_dir}" --target clean
    set +e
    cmake --build "${build_dir}" --target native_mpy
    first_stage_status=$?
    set -e
    if [[ ! -f "${build_dir}/ROSMicroPy.normalized.o" ]]; then
        exit "${first_stage_status}"
    fi

    externs_file="${build_dir}/firmware_externs.ld"
    FIRMWARE_ELF="${firmware_elf}" BUILD_DIR="${build_dir}" TARGET="${target}" "${script_dir}/generate_mpy_externs.sh" "${externs_file}"
    cmake_args+=(-DMPY_EXTERNS_FILE="${externs_file}")
else
    cmake_args+=(-DMPY_EXTERNS_FILE:FILEPATH=)
fi

cmake -S "${script_dir}" -B "${build_dir}" \
    "${cmake_args[@]}"

cmake --build "${build_dir}" --target native_mpy

printf 'Built %s\n' "${build_dir}/ROSMicroPy.mpy"
