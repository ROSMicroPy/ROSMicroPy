set(IDF_TARGET esp32)
#set(IDF_TARGET esp32s3)

set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.microros
    boards/sdkconfig.base
    boards/sdkconfig.ble
    boards/RMP_WROVER_B/sdkconfig.board
    boards/sdkconfig.240mhz
#    boards/sdkconfig.int32
#    boards/sdkconfig.compiler.debug
#    boards/sdkconfig.usb
)

if(MICROPY_BOARD_VARIANT STREQUAL "D2WD")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/RMP_WROVER_B/sdkconfig.d2wd
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
        boards/RMP_WROVER_B/sdkconfig.ota
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_BOARD_NAME="RosMicroPy WROVER-B"
    )
endif()

if(MICROPY_BOARD_VARIANT STREQUAL "SPIRAM")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/sdkconfig.spiram
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_BOARD_NAME="RosMicroPy WROVER-B with SPIRAM"
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

