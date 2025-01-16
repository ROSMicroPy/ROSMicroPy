
cd /opt/rosmicropy/components/micro_ros_espidf_component

idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CAM_GENERIC fullclean
idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CAM_GENERIC clean

make -f libmicroros.mk clean
cd /opt/rosmicropy
sh mkdirs.sh
cd /opt/rosmicropy/micropython/ports/esp32
rm -rf build

idf.py -D MICROPY_BOARD_DIR=/opt/rosmicropy/boards/esp32/RMP_CAM_GENERIC build

cp build/micropython.bin /opt/rosmicropy/release/rmp_cam_generic.bin
cp build/micropython.elf /opt/rosmicropy/release/rmp_cam_generic.elf
cp build/micropython.map /opt/rosmicropy/release/rmp_cam_generic.map
cp build/bootloader/bootloader.bin /opt/rosmicropy/release/rmp_cam_generic_bootloader.bin
cp build/partition_table/partition-table.bin /opt/rosmicropy/release/rmp_cam_generic_partition-table.bin
