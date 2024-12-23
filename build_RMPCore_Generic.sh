#!/bin/bash

cd /opt/rosmicropy/micropython/ports/esp32

idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CORE_GENERIC fullclean
idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CORE_GENERIC clean

rm -rf build
rm -rf managed_components

cd /opt/rosmicropy/
sh mkdirs.sh
cd -

idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CORE_GENERIC build
cp build/micropython.bin /opt/rosmicropy/release/rmp_core_generic.bin
cp build/micropython.elf /opt/rosmicropy/release/rmp_core_generic.elf
cp build/micropython.map /opt/rosmicropy/release/rmp_core_generic.map
cp build/bootloader/bootloader.bin /opt/rosmicropy/release/rmp_core_generic_bootloader.bin
cp build/partition_table/partition-table.bin /opt/rosmicropy/release/rmp_core_generic_partition-table.bin

