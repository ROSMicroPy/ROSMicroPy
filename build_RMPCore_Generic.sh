#!/bin/bash

cd /opt/rosmicropy/components/micro_ros_espidf_component/
make -f libmicroros.mk clean
cd /opt/rosmicropy
sh mkdirs.sh
cd /opt/rosmicropy/micropython/ports/esp32
rm -rf build
idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CORE_GENERIC build
cp build/micropython.bin /opt/rosmicropy/release/rmp_core_generic.bin
cp build/micropython.elf /opt/rosmicropy/release/rmp_core_generic.elf
cp build/micropython.map /opt/rosmicropy/release/rmp_core_generic.map
cp build/bootloader/bootloader.bin /opt/rosmicropy/release/rmp_core_generic_bootloader.bin
cp build/partition_table/partition-table.bin /opt/rosmicropy/release/rmp_core_generic_partition-table
