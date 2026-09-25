// This configuration is for a generic ESP32C5 board with 4MiB (or more) of flash.

#define MICROPY_HW_BOARD_NAME               "ESP32C5 module"
#define MICROPY_HW_MCU_NAME                 "ESP32C5"

#define MICROPY_HW_ENABLE_SDCARD            (0)
#define MICROPY_PY_MACHINE_I2S              (0)

// Keep the MicroPython submodule unpatched with IDF 5.5.x.  Upstream
// v1.28.0's NimBLE source does not compile against this IDF release, and
// ROSMicroPy does not require the bluetooth module.
#define MICROPY_PY_BLUETOOTH                (0)

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
#define MICROPY_HW_ENABLE_UART_REPL         (1)
