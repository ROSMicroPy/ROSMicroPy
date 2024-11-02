set(IDF_TARGET esp32s3)

get_filename_component(BOARD_COMMON_DIR $(BOARD_DIR)/.. ABSOLUTE)
get_filename_component(MODULE_DIR ../../../../modules ABSOLUTE)

set(SDKCONFIG_DEFAULTS
    ${BOARD_COMMON_DIR}/sdkconfig.menuconfig
    boards/sdkconfig.base
    boards/sdkconfig.ble
    boards/sdkconfig.usb
    boards/sdkconfig.spiram_sx
    ${BOARD_DIR}/sdkconfig.board
    ${BOARD_COMMON_DIR}/sdkconfig.microros
)

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


set(MICROPY_BOARD_VARIANT "SPIRAM_OCT")

if(MICROPY_BOARD_VARIANT STREQUAL "SPIRAM_OCT")
    set(SDKCONFIG_DEFAULTS
        ${SDKCONFIG_DEFAULTS}
        boards/sdkconfig.240mhz
        boards/sdkconfig.spiram_oct
    )

    list(APPEND MICROPY_DEF_BOARD
        MICROPY_HW_BOARD_NAME="ESP32S3 RosMicroPy ESP Cam with Oct RAM"
    )
endif()
