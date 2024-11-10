set(IDF_TARGET esp32c6)


set(MICROPY_BOARD RMP_CORE_C6)

get_filename_component(BOARD_COMMON_DIR ${CMAKE_CURRENT_LIST_DIR}/.. ABSOLUTE)
get_filename_component(MODULE_DIR ../../../modules ABSOLUTE)
get_filename_component(COMPONENT_DIR ../../../components ABSOLUTE)

message("Board Common Dir ${BOARD_COMMON_DIR}")
message("Module Dir ${MODULE_DIR}")

list(APPEND USER_C_MODULES 
    ${MODULE_DIR}/libROSMicroPy/micropython.cmake
    ${MODULE_DIR}/micropython-helpers/micropython.cmake
)

# set(SDKCONFIG_DEFAULTS
#     boards/sdkconfig.base
#     ${SDKCONFIG_IDF_VERSION_SPECIFIC}
#     boards/sdkconfig.c6
#     boards/sdkconfig.ble
# )

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    ${SDKCONFIG_IDF_VERSION_SPECIFIC}
    boards/sdkconfig.c6
    boards/sdkconfig.usb
    boards/sdkconfig.ble
    ${CMAKE_CURRENT_LIST_DIR}/sdkconfig.board
)

if(MICROPY_BOARD_VARIANT STREQUAL "SPIRAM_OCT")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/sdkconfig.240mhz
        boards/sdkconfig.spiram_oct
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_BOARD_NAME="Generic ESP32S3 module with Octal-SPIRAM"
    )
endif()

if(MICROPY_BOARD_VARIANT STREQUAL "FLASH_4M")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/ESP32_GENERIC_S3/sdkconfig.flash_4m
    )
endif()

get_filename_component(MAIN2_COMPONENT_DIR ${MICROPY_BOARD_DIR}/main2 ABSOLUTE)

list(APPEND EXTRA_COMPONENT_DIRS
    ${MAIN2_COMPONENT_DIR}
)