   esptool.py  -b 460800 --before default_reset --after hard_reset --chip esp32s3  \
    write_flash --flash_size 4MB --flash_freq 80m \
    0x00 bootloader.bin \
    0x8000 micropython.bin \
    0x10000 partition-table.bin
