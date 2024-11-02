
set(IDF_TARGET esp32)
#set(IDF_TARGET esp32s3)

get_filename_component(BOARD_COMMON_DIR $(BOARD_DIR)/.. ABSOLUTE)
get_filename_component(MODULE_DIR ../../../../modules ABSOLUTE)

set(SDKCONFIG_DEFAULTS 
    ${BOARD_COMMON_DIR}/sdkconfig.microros
    ${BOARD_COMMON_DIR}/sdkconfig.cam
    boards/sdkconfig.base
    boards/sdkconfig.ble
    boards/sdkconfig.240mhz
    boards/sdkconfig.spiram

)


list (USER_C_MODULE APPEND
    ${MODULE_DIR}/libROSMicroPy
    ${MODULE_DIR}/libROSMicroPyESPCAM
    ${MODULE_DIR}/micropython-helpers 
)

list(APPEND COMPONENT_DIR
    $(BOARD_DIR)/main
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

