#ifndef MICROPY_HW_BOARD_NAME
// Can be set by mpconfigboard.cmake.
#define MICROPY_HW_BOARD_NAME               "Generic ESP32S3 module"
#endif
#define MICROPY_HW_MCU_NAME                 "ESP32S3"

// Keep the MicroPython submodule unpatched with IDF 5.5.x.  Upstream
// v1.28.0's NimBLE source does not compile against this IDF release, and
// ROSMicroPy does not require the bluetooth module.
#define MICROPY_PY_BLUETOOTH                (0)

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
#define MICROPY_HW_ENABLE_UART_REPL         (1)

#define MICROPY_HW_I2C0_SCL                 (9)
#define MICROPY_HW_I2C0_SDA                 (8)
