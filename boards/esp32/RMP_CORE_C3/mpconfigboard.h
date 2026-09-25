// This configuration is for a generic ESP32C3 board with 4MiB (or more) of flash.

#define MICROPY_HW_BOARD_NAME               "ESP32C3 module"
#define MICROPY_HW_MCU_NAME                 "ESP32C3"

#define MICROPY_HW_ENABLE_SDCARD            (0)

// Keep the MicroPython submodule unpatched with IDF 5.5.x.  Upstream
// v1.28.0's NimBLE source does not compile against this IDF release, and
// ROSMicroPy does not require the bluetooth module.
#define MICROPY_PY_BLUETOOTH                (0)

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
#define MICROPY_HW_ENABLE_UART_REPL         (1)
