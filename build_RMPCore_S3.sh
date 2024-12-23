cd /opt/rosmicropy/micropython/ports/esp32

idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CORE_S3 fullclean
idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CORE_S3 clean

rm -rf build
rm -rf managed_components
cd /opt/rosmicropy/
sh ./mkdirs.sh
cd -

idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CORE_S3 build

cp build/micropython.bin /opt/rosmicropy/release/rmp_core_s3.bin
cp build/micropython.elf /opt/rosmicropy/release/rmp_core_s3.elf
cp build/micropython.map /opt/rosmicropy/release/rmp_core_s3.map
cp build/bootloader/bootloader.bin /opt/rosmicropy/release/rmp_core_s3_bootloader.bin
cp build/partition_table/partition-table.bin /opt/rosmicropy/release/rmp_core_s3_partition-table.bin

