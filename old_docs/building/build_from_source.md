### Clone this repository
* `git clone https://github.com/rosmicropy/ROSMicroPy.git`
* `cd ROSMicroPy`
* `git submodule update --init --recursive`

### Building ROSMicroPy
* cd micropython/ports/esp32
* rm -rf /build
* idf.py -D MICROPY_BOARD_DIR=../../../boards/esp32/*{boardname}* build
  * Where Board name isa subdirectoryin ROSMicroPy/boards/esp32
* Upon successful build, flash the ESP32 board with
* idf.py -D MICROPY_BOARD_DIR=../../../boards/esp32/*{boardname}* flash
