set(IDF_TARGET esp32s3)

set(LVGL_DRIVER_ESP32S3_8048S050C 1)


get_filename_component(BOARD_COMMON_DIR ${CMAKE_CURRENT_LIST_DIR}/.. ABSOLUTE)
get_filename_component(MODULE_DIR ../../../modules ABSOLUTE)
message("Board Common Dir ${BOARD_COMMON_DIR}")
message("Module Dir ${MODULE_DIR}")

list(APPEND IDF_COMPONENTS
  json
)


message("User C Modules ${USER_C_MODULES}")

get_filename_component(MAIN2_COMPONENT_DIR ${MICROPY_BOARD_DIR}/main2 ABSOLUTE)

list(APPEND COMPONENT_DIRS
    ${MAIN2_COMPONENT_DIR}
)

list(APPEND USER_C_MODULES 
    ${MODULE_DIR}/libROSMicroPy/micropython.cmake
    ${MODULE_DIR}/micropython-helpers/micropython.cmake
    ${MODULE_DIR}/libMicroPy_JSONForms/micropython.cmake
    ${MODULE_DIR}/lib_ROSMicroPyWidgets/micropython.cmake
  
)

set(SDKCONFIG_DEFAULTS
    ${BOARD_COMMON_DIR}/sdkconfig.menuconfig
    boards/sdkconfig.base
    boards/sdkconfig.usb
    boards/sdkconfig.ble
    boards/sdkconfig.spiram_sx
    ${MICROPY_BOARD_DIR}/sdkconfig.board
    ${BOARD_COMMON_DIR}/sdkconfig.lvgl
    ${BOARD_COMMON_DIR}/sdkconfig.microros
)

set(MICROPY_BOARD_VARIANT "SPIRAM_OCT")

if(MICROPY_BOARD_VARIANT STREQUAL "SPIRAM_OCT")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/sdkconfig.240mhz
        boards/sdkconfig.spiram_oct
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_BOARD_NAME="ESP32S3 RosMicroPy LCD with Oct RAM"
    )
endif()
