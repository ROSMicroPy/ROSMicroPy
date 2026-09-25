#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOARD_DIR="${ROOT_DIR}/boards/esp32/RMP_CORE_C5"
ESP32_PORT_DIR="${ROOT_DIR}/micropython/ports/esp32"
RELEASE_DIR="${ROOT_DIR}/release"

cd "${ESP32_PORT_DIR}"

rm -rf build managed_components

cd "${ROOT_DIR}"
sh ./mkdirs.sh

make -C "${ROOT_DIR}/components/micro_ros_espidf_component" -f libmicroros.mk clean
TARGET=esp32c5 "${ROOT_DIR}/components/prepare_microros.sh"

cd "${ESP32_PORT_DIR}"

idf.py -D MICROPY_BOARD_DIR="${BOARD_DIR}" build

mkdir -p "${RELEASE_DIR}"
cp build/micropython.bin "${RELEASE_DIR}/rmp_core_c5.bin"
cp build/micropython.elf "${RELEASE_DIR}/rmp_core_c5.elf"
cp build/micropython.map "${RELEASE_DIR}/rmp_core_c5.map"
cp build/bootloader/bootloader.bin "${RELEASE_DIR}/rmp_core_c5_bootloader.bin"
cp build/partition_table/partition-table.bin "${RELEASE_DIR}/rmp_core_c5_partition-table.bin"
