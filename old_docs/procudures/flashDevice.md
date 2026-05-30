# Flash Device

    Currently only ESP32S* devices are supported and tested, YMMV with the ESP32C* devices, plans are in the works to also support ESP32C*, STM32 and Unix

## ESP Devices
 The release directory will contain the latest binary build for that version.
 If you have idf.py or esptool.py (components of the ESP-IDF SDK) then you can flash directly to your device. If you rather not install the ESP SDK, you can use the [Development Container](../containerSuppoert/containerDevEnv.md) to flash the code to your device as it provides all the required tools.

In either container, change directories to the root of the project.

esptool.py  write_flash --flash_mode dio --flash_size detect  40m 0x1000 release/mbits-esp32s2-wrover.bin

Once programed, you be able to see the Device in Thonny and have access to the REPL prompt in the bottom pane. If Thonny refuses to connect to the device it maybe that the container or esptool is still holding onto the serial port. If this occurs, disconnect then reconnect the device from the USB port.

**Linux users: You will need to add your user to the dialout group to be able to access the serial port, also if you have the brltty package installed you will probably need to remove it as it grabs the serial ports at boot time**
