message("RMP ESPCAM Controller Board")
# Set location of base MicroPython directory.

if(NOT MICROPY_DIR)
    get_filename_component(MICROPY_DIR ${CMAKE_CURRENT_LIST_DIR}/../../../micropython ABSOLUTE)
endif()
message("MICROPY_DIR ${MICROPY_DIR}")

# Set location of the ESP32 port directory.
if(NOT MICROPY_PORT_DIR)
    get_filename_component(MICROPY_PORT_DIR ${MICROPY_DIR}/ports/esp32 ABSOLUTE)
endif()
message("MICROPY_PORT_DIR ${MICROPY_PORT_DIR}")

list(APPEND IDF_COMPONENTS
  json
)

#include(${MICROPY_PORT_DIR}/esp32_common.cmake)
