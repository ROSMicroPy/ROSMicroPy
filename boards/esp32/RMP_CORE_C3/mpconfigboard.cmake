set(IDF_TARGET esp32c3)
set(MICROPY_BOARD RMP_CORE_C3)

get_filename_component(BOARD_COMMON_DIR ${CMAKE_CURRENT_LIST_DIR}/.. ABSOLUTE)
get_filename_component(COMPONENTS_DIR ../../../components ABSOLUTE)

message("Board Common Dir ${BOARD_COMMON_DIR}")
message("Components Dir ${COMPONENTS_DIR}")

list(APPEND USER_C_MODULES
    ${COMPONENTS_DIR}/libROSMicroPy/micropython.cmake
    ${COMPONENTS_DIR}/micropython-helpers/micropython.cmake
)

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    boards/sdkconfig.riscv
    ${SDKCONFIG_IDF_VERSION_SPECIFIC}
    boards/ESP32_GENERIC_C3/sdkconfig.c3usb
    ${CMAKE_CURRENT_LIST_DIR}/sdkconfig.board
)

get_filename_component(MAIN2_COMPONENT_DIR ${MICROPY_BOARD_DIR}/main2 ABSOLUTE)

list(APPEND EXTRA_COMPONENT_DIRS
    ${MAIN2_COMPONENT_DIR}
)
