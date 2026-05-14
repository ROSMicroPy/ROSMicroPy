// Both of these can be set by mpconfigboard.cmake if a BOARD_VARIANT is
// specified.

#ifndef MICROPY_HW_BOARD_NAME
#define MICROPY_HW_BOARD_NAME "Generic ESP32 module"
#endif

#ifndef MICROPY_HW_MCU_NAME
#define MICROPY_HW_MCU_NAME "ESP32"
#endif

// Keep the MicroPython submodule unpatched with IDF 5.5.x.  Upstream
// v1.28.0's NimBLE source does not compile against this IDF release, and
// ROSMicroPy does not require the bluetooth module.
#define MICROPY_PY_BLUETOOTH (0)
