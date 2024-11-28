
set(IDF_TARGET esp32)
#set(IDF_TARGET esp32s3)
message("MicroPython Board Dir ${MICROPY_BOARD_DIR}")
get_filename_component(BOARD_COMMON_DIR ${MICROPY_BOARD_DIR}/.. ABSOLUTE)
get_filename_component(MODULE_DIR ../../../modules ABSOLUTE)

message("Board Common Dir ${BOARD_COMMON_DIR}")
message("Module Dir ${MODULE_DIR}")

set(SDKCONFIG_DEFAULTS 
    ${BOARD_COMMON_DIR}/sdkconfig.microros
#    ${BOARD_COMMON_DIR}/sdkconfig.cam
    boards/sdkconfig.base
    boards/sdkconfig.ble
    boards/sdkconfig.240mhz
    boards/sdkconfig.spiram

)


list(APPEND USER_C_MODULES 
    ${MODULE_DIR}/libROSMicroPy/micropython.cmake
    ${MODULE_DIR}/libROSMicroPyESPCAM/micropython.cmake
    ${MODULE_DIR}/micropython-helpers/micropython.cmake
)


get_filename_component(MAIN2_COMPONENT_DIR ${MICROPY_BOARD_DIR}/main2 ABSOLUTE)

list(APPEND EXTRA_COMPONENT_DIRS
    ${MAIN2_COMPONENT_DIR}
)

if(MICROPY_BOARD_VARIANT STREQUAL "D2WD")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/ESP32_GENERIC/sdkconfig.d2wd
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_MCU_NAME="ESP32-D2WD"
        # Disable some options to reduce firmware size.
        MICROPY_OPT_COMPUTED_GOTO=0
        MICROPY_PY_NETWORK_LAN=0
    )
endif()

if(MICROPY_BOARD_VARIANT STREQUAL "OTA")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/ESP32_GENERIC/sdkconfig.ota
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_BOARD_NAME="Generic ESP32 module with OTA"
    )
endif()

if(MICROPY_BOARD_VARIANT STREQUAL "SPIRAM")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/sdkconfig.spiram
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_BOARD_NAME="Generic ESP32 module with SPIRAM"
    )
endif()

if(MICROPY_BOARD_VARIANT STREQUAL "UNICORE")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/ESP32_GENERIC/sdkconfig.unicore
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_MCU_NAME="ESP32-UNICORE"
    )
endif()

