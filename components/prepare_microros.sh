#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
component_dir="${script_dir}/micro_ros_espidf_component"
build_dir="${BUILD_DIR:-${script_dir}/build-microros}"
target="${TARGET:-esp32s3}"
idf_path="${IDF_PATH:-/opt/esp/idf}"

case "${target}" in
    esp3-s3|esp32-s3)
        target="esp32s3"
        ;;
    esp32s3|esp32s2|esp32|esp32c3)
        ;;
    *)
        printf 'Unsupported TARGET=%s\n' "${target}" >&2
        printf 'Supported targets: esp32s3, esp32s2, esp32, esp32c3\n' >&2
        exit 2
        ;;
esac

case "${target}" in
    esp32s3)
        cc="${CC:-xtensa-esp32s3-elf-gcc}"
        cxx="${CXX:-xtensa-esp32s3-elf-g++}"
        ;;
    esp32s2)
        cc="${CC:-xtensa-esp32s2-elf-gcc}"
        cxx="${CXX:-xtensa-esp32s2-elf-g++}"
        ;;
    esp32)
        cc="${CC:-xtensa-esp32-elf-gcc}"
        cxx="${CXX:-xtensa-esp32-elf-g++}"
        ;;
    esp32c3)
        cc="${CC:-riscv32-esp-elf-gcc}"
        cxx="${CXX:-riscv32-esp-elf-g++}"
        ;;
esac

mkdir -p "${build_dir}/config"
cp "${script_dir}/native/sdkconfig.h" "${build_dir}/config/sdkconfig.h"

if [[ -d "${component_dir}/micro_ros_src/install" ]] \
    && { [[ ! -f "${component_dir}/include/rcl/rcl.h" && ! -f "${component_dir}/include/rcl/rcl/rcl.h" ]] \
        || [[ ! -f "${component_dir}/libmicroros.a" ]]; }; then
    printf 'Found partial micro-ROS install output; cleaning before rebuild.\n' >&2
    make -C "${component_dir}" -f libmicroros.mk clean
fi

idf_includes=""
add_include() {
    if [[ -d "$1" ]]; then
        idf_includes="${idf_includes} -I$1"
    fi
}

add_include "${idf_path}/components/newlib/platform_include"
add_include "${idf_path}/components/freertos/config/include"
add_include "${idf_path}/components/freertos/config/include/freertos"
add_include "${idf_path}/components/freertos/config/xtensa/include"
add_include "${idf_path}/components/freertos/FreeRTOS-Kernel/include"
add_include "${idf_path}/components/freertos/FreeRTOS-Kernel/portable/xtensa/include"
add_include "${idf_path}/components/freertos/FreeRTOS-Kernel/portable/xtensa/include/freertos"
add_include "${idf_path}/components/freertos/esp_additions/include"
add_include "${idf_path}/components/esp_common/include"
add_include "${idf_path}/components/esp_system/include"
add_include "${idf_path}/components/esp_system/port/include"
add_include "${idf_path}/components/esp_hw_support/include"
add_include "${idf_path}/components/esp_hw_support/port/include"
add_include "${idf_path}/components/esp_hw_support/port/${target}/include"
add_include "${idf_path}/components/hal/include"
add_include "${idf_path}/components/hal/${target}/include"
add_include "${idf_path}/components/soc/include"
add_include "${idf_path}/components/soc/${target}/include"
add_include "${idf_path}/components/soc/${target}/register"
add_include "${idf_path}/components/log/include"
add_include "${idf_path}/components/heap/include"
add_include "${idf_path}/components/esp_rom/include"
add_include "${idf_path}/components/esp_rom/${target}/include"
add_include "${idf_path}/components/esp_netif/include"
add_include "${idf_path}/components/esp_wifi/include"
add_include "${idf_path}/components/esp_event/include"
add_include "${idf_path}/components/esp_eth/include"
add_include "${idf_path}/components/esp_driver_gpio/include"
add_include "${idf_path}/components/esp_driver_spi/include"
add_include "${idf_path}/components/esp_partition/include"
add_include "${idf_path}/components/nvs_flash/include"
add_include "${idf_path}/components/lwip/include"
add_include "${idf_path}/components/lwip/port/include"
add_include "${idf_path}/components/lwip/port/freertos/include"
add_include "${idf_path}/components/lwip/port/esp32xx/include"
add_include "${idf_path}/components/lwip/lwip/src/include"
add_include "${idf_path}/components/pthread/include"
add_include "${idf_path}/components/xtensa/include"
add_include "${idf_path}/components/xtensa/${target}/include"

make -C "${component_dir}" -f libmicroros.mk \
    X_CC="${cc}" \
    X_CXX="${cxx}" \
    X_AR="${AR:-${cc/gcc/ar}}" \
    X_STRIP="${STRIP:-${cc/gcc/strip}}" \
    X_CFLAGS="-Os -ffunction-sections -fdata-sections -DIDF_VER=\\\"rosmicropy-components\\\"" \
    X_CXXFLAGS="-Os -ffunction-sections -fdata-sections -DIDF_VER=\\\"rosmicropy-components\\\"" \
    C_STANDARD=17 \
    MIDDLEWARE="${MIDDLEWARE:-microxrcedds}" \
    BUILD_DIR="${build_dir}" \
    IDF_INCLUDES="${idf_includes} -I${component_dir}/include_override" \
    IDF_PATH="${idf_path}" \
    IDF_TARGET="${target}" \
    IDF_VERSION_MAJOR="${IDF_VERSION_MAJOR:-5}" \
    IDF_VERSION_MINOR="${IDF_VERSION_MINOR:-5}" \
    APP_COLCON_META="${APP_COLCON_META:-}" \
    EXTRA_ROS_PACKAGES="${EXTRA_ROS_PACKAGES:-${component_dir}/extra_packages}"

if [[ ! -f "${component_dir}/include/rcl/rcl.h" && ! -f "${component_dir}/include/rcl/rcl/rcl.h" ]] \
    || [[ ! -f "${component_dir}/libmicroros.a" ]]; then
    printf 'micro-ROS preparation did not produce rcl headers and libmicroros.a\n' >&2
    exit 1
fi

printf 'Prepared %s/include and %s/libmicroros.a\n' "${component_dir}" "${component_dir}"
