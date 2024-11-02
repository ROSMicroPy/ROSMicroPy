message("RMP LCD Controller Board")
# Set location of base MicroPython directory.
if(NOT MICROPY_DIR)
    get_filename_component(MICROPY_DIR ${CMAKE_CURRENT_LIST_DIR}/../../.. ABSOLUTE)
endif()

# Set location of the ESP32 port directory.
if(NOT MICROPY_PORT_DIR)
    get_filename_component(MICROPY_PORT_DIR ${MICROPY_DIR}/ports/esp32 ABSOLUTE)
endif()

list(APPEND IDF_COMPONENTS
  json
)

set(LVGL_DRIVER_ESP32S3_8048S050C 1)

include(${MICROPY_PORT_DIR}/esp32_common.cmake)
