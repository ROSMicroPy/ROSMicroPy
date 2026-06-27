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
    esp32s3|esp32s2|esp32|esp32c3|esp32c5|esp32c6)
        ;;
    *)
        printf 'Unsupported TARGET=%s\n' "${target}" >&2
        printf 'Supported targets: esp32s3, esp32s2, esp32, esp32c3, esp32c5, esp32c6\n' >&2
        exit 2
        ;;
esac

case "${target}" in
    esp32s3)
        cc="${CC:-xtensa-esp32s3-elf-gcc}"
        cxx="${CXX:-xtensa-esp32s3-elf-g++}"
        arch="xtensa"
        ;;
    esp32s2)
        cc="${CC:-xtensa-esp32s2-elf-gcc}"
        cxx="${CXX:-xtensa-esp32s2-elf-g++}"
        arch="xtensa"
        ;;
    esp32)
        cc="${CC:-xtensa-esp32-elf-gcc}"
        cxx="${CXX:-xtensa-esp32-elf-g++}"
        arch="xtensa"
        ;;
    esp32c3|esp32c5|esp32c6)
        cc="${CC:-riscv32-esp-elf-gcc}"
        cxx="${CXX:-riscv32-esp-elf-g++}"
        arch="riscv"
        ;;
esac

mkdir -p "${build_dir}/config"
cp "${script_dir}/native/sdkconfig.h" "${build_dir}/config/sdkconfig.h"
{
    printf '\n#undef CONFIG_IDF_TARGET_ESP32S3\n'
    printf '#undef CONFIG_IDF_TARGET_ESP32S2\n'
    printf '#undef CONFIG_IDF_TARGET_ESP32C3\n'
    printf '#undef CONFIG_IDF_TARGET_ESP32C5\n'
    printf '#undef CONFIG_IDF_TARGET_ESP32C6\n'
    printf '#undef CONFIG_IDF_TARGET_ESP32\n'
    printf '#undef CONFIG_IDF_TARGET\n'
    printf '#define CONFIG_IDF_TARGET "%s"\n' "${target}"
    case "${target}" in
        esp32s3)
            printf '#define CONFIG_IDF_TARGET_ESP32S3 1\n'
            printf '#undef CONFIG_FREERTOS_NUMBER_OF_CORES\n'
            printf '#define CONFIG_FREERTOS_NUMBER_OF_CORES 2\n'
            printf '#undef CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ\n'
            printf '#define CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ 240\n'
            ;;
        esp32s2)
            printf '#define CONFIG_IDF_TARGET_ESP32S2 1\n'
            printf '#undef CONFIG_FREERTOS_NUMBER_OF_CORES\n'
            printf '#define CONFIG_FREERTOS_NUMBER_OF_CORES 1\n'
            printf '#define CONFIG_ESP_SYSTEM_SINGLE_CORE_MODE 1\n'
            printf '#undef CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ\n'
            printf '#define CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ 240\n'
            ;;
        esp32)
            printf '#define CONFIG_IDF_TARGET_ESP32 1\n'
            printf '#undef CONFIG_FREERTOS_NUMBER_OF_CORES\n'
            printf '#define CONFIG_FREERTOS_NUMBER_OF_CORES 2\n'
            printf '#undef CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ\n'
            printf '#define CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ 240\n'
            ;;
        esp32c3|esp32c6)
            upper_target="$(printf '%s' "${target}" | tr '[:lower:]' '[:upper:]')"
            printf '#define CONFIG_IDF_TARGET_%s 1\n' "${upper_target}"
            printf '#undef CONFIG_FREERTOS_NUMBER_OF_CORES\n'
            printf '#define CONFIG_FREERTOS_NUMBER_OF_CORES 1\n'
            printf '#define CONFIG_ESP_SYSTEM_SINGLE_CORE_MODE 1\n'
            printf '#undef CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ\n'
            printf '#define CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ 160\n'
            ;;
        esp32c5)
            printf '#define CONFIG_IDF_TARGET_ESP32C5 1\n'
            printf '#undef CONFIG_FREERTOS_NUMBER_OF_CORES\n'
            printf '#define CONFIG_FREERTOS_NUMBER_OF_CORES 1\n'
            printf '#define CONFIG_ESP_SYSTEM_SINGLE_CORE_MODE 1\n'
            printf '#undef CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ\n'
            printf '#define CONFIG_ESP_DEFAULT_CPU_FREQ_MHZ 240\n'
            ;;
    esac
} >> "${build_dir}/config/sdkconfig.h"

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
add_include "${idf_path}/components/freertos/config/${arch}/include"
add_include "${idf_path}/components/freertos/FreeRTOS-Kernel/include"
add_include "${idf_path}/components/freertos/FreeRTOS-Kernel/portable/${arch}/include"
add_include "${idf_path}/components/freertos/FreeRTOS-Kernel/portable/${arch}/include/freertos"
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
add_include "${idf_path}/components/${arch}/include"
add_include "${idf_path}/components/${arch}/${target}/include"

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
