cmake_minimum_required(VERSION 3.16)

project(rosmicropy_native_mpy C CXX)

set(MPY_DIR "${CMAKE_CURRENT_LIST_DIR}/../micropython" CACHE PATH "Path to the MicroPython source tree")
set(IDF_PATH "$ENV{IDF_PATH}" CACHE PATH "Path to ESP-IDF")
set(MPY_ARCH "xtensawin" CACHE STRING "MicroPython native .mpy architecture")
set(MPY_TARGET "esp32s3" CACHE STRING "Target board/chip family")
set(MPY_MODULE_NAME "ROSMicroPy" CACHE STRING "Name of the generated native .mpy module")

set_property(CACHE MPY_ARCH PROPERTY STRINGS
    x86
    x64
    armv6m
    armv7m
    armv7emsp
    armv7emdp
    xtensa
    xtensawin
)

set_property(CACHE MPY_TARGET PROPERTY STRINGS
    host
    esp32
    esp32s2
    esp32s3
)

set(NATMOD_DIR "${CMAKE_CURRENT_LIST_DIR}")
set(ROSMICROPY_DIR "${NATMOD_DIR}/libROSMicroPy")
set(MP_HELPERS_DIR "${NATMOD_DIR}/micropython-helpers")
set(NATMOD_MICROROS_DIR "${NATMOD_DIR}/micro_ros_espidf_component")

message(STATUS "Evaluating natmod components")
message(STATUS "  target: ${MPY_TARGET}")
message(STATUS "  native .mpy arch: ${MPY_ARCH}")
message(STATUS "  libROSMicroPy: ${ROSMICROPY_DIR}")
message(STATUS "  micropython-helpers: ${MP_HELPERS_DIR}")
if(EXISTS "${NATMOD_MICROROS_DIR}/CMakeLists.txt")
    message(STATUS "  micro_ros_espidf_component: ${NATMOD_MICROROS_DIR}")
else()
    message(WARNING "  micro_ros_espidf_component: not found; initialise the submodule before building firmware bindings")
endif()

find_package(Python3 REQUIRED COMPONENTS Interpreter)

set(MPY_LD "${CMAKE_CURRENT_LIST_DIR}/tools/mpy_ld_rosmicropy.py" CACHE FILEPATH "Native .mpy linker")
set(MPY_TOOL "${MPY_DIR}/tools/mpy-tool.py")
set(MPY_CROSS "${MPY_DIR}/mpy-cross/build/mpy-cross")
set(MPY_TOOL_PYTHONPATH "${MPY_DIR}/tools:${MPY_DIR}/py:$ENV{PYTHONPATH}")
set(MICROROS_INCLUDE_DIR "${NATMOD_MICROROS_DIR}/include" CACHE PATH "Path to generated micro-ROS headers")
set(MICROROS_LIB "${NATMOD_MICROROS_DIR}/libmicroros.a" CACHE FILEPATH "Path to generated libmicroros archive")
set(MPY_EXTERNS_FILE "" CACHE FILEPATH "Optional linker script with fixed-address firmware symbols for native .mpy linking")

if(NOT EXISTS "${MPY_LD}")
    message(FATAL_ERROR "mpy_ld.py not found at ${MPY_LD}; set -DMPY_DIR=/path/to/micropython")
endif()

if(NOT EXISTS "${MPY_TOOL}")
    message(FATAL_ERROR "mpy-tool.py not found at ${MPY_TOOL}; set -DMPY_DIR=/path/to/micropython")
endif()

if(NOT EXISTS "${MPY_CROSS}")
    message(FATAL_ERROR "mpy-cross not found at ${MPY_CROSS}; build it first with: make -C ${MPY_DIR}/mpy-cross")
endif()

set(MPY_CC gcc)
set(MPY_CXX g++)
set(MPY_FLOAT_IMPL double)
set(MPY_ARCH_FLAGS -fno-stack-protector)

if(MPY_ARCH STREQUAL "x86")
    set(MPY_ARCH_FLAGS -m32 -fno-stack-protector)
elseif(MPY_ARCH STREQUAL "x64")
    set(MPY_ARCH_FLAGS -fno-stack-protector)
elseif(MPY_ARCH STREQUAL "armv6m")
    set(MPY_CC arm-none-eabi-gcc)
    set(MPY_CXX arm-none-eabi-g++)
    set(MPY_ARCH_FLAGS -mthumb -mcpu=cortex-m0)
    set(MPY_FLOAT_IMPL none)
elseif(MPY_ARCH STREQUAL "armv7m")
    set(MPY_CC arm-none-eabi-gcc)
    set(MPY_CXX arm-none-eabi-g++)
    set(MPY_ARCH_FLAGS -mthumb -mcpu=cortex-m3)
    set(MPY_FLOAT_IMPL none)
elseif(MPY_ARCH STREQUAL "armv7emsp")
    set(MPY_CC arm-none-eabi-gcc)
    set(MPY_CXX arm-none-eabi-g++)
    set(MPY_ARCH_FLAGS -mthumb -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard)
    set(MPY_FLOAT_IMPL float)
elseif(MPY_ARCH STREQUAL "armv7emdp")
    set(MPY_CC arm-none-eabi-gcc)
    set(MPY_CXX arm-none-eabi-g++)
    set(MPY_ARCH_FLAGS -mthumb -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard)
    set(MPY_FLOAT_IMPL double)
elseif(MPY_ARCH STREQUAL "xtensa")
    set(MPY_CC xtensa-lx106-elf-gcc)
    set(MPY_CXX xtensa-lx106-elf-g++)
    set(MPY_ARCH_FLAGS -mforce-l32)
    set(MPY_FLOAT_IMPL none)
elseif(MPY_ARCH STREQUAL "xtensawin")
    if(MPY_TARGET STREQUAL "esp32s3")
        set(MPY_CC xtensa-esp32s3-elf-gcc)
        set(MPY_CXX xtensa-esp32s3-elf-g++)
    elseif(MPY_TARGET STREQUAL "esp32s2")
        set(MPY_CC xtensa-esp32s2-elf-gcc)
        set(MPY_CXX xtensa-esp32s2-elf-g++)
    else()
        set(MPY_CC xtensa-esp32-elf-gcc)
        set(MPY_CXX xtensa-esp32-elf-g++)
    endif()
    set(MPY_ARCH_FLAGS -mlongcalls -mno-text-section-literals)
    set(MPY_FLOAT_IMPL float)
else()
    message(FATAL_ERROR "Unsupported MPY_ARCH=${MPY_ARCH}")
endif()

find_program(MPY_CC_PATH "${MPY_CC}")
if(NOT MPY_CC_PATH)
    message(FATAL_ERROR "Compiler ${MPY_CC} not found for MPY_TARGET=${MPY_TARGET}")
endif()
set(MPY_CC "${MPY_CC_PATH}")
message(STATUS "  native compiler: ${MPY_CC}")

find_program(MPY_CXX_PATH "${MPY_CXX}")
if(NOT MPY_CXX_PATH)
    message(FATAL_ERROR "Compiler ${MPY_CXX} not found for MPY_TARGET=${MPY_TARGET}")
endif()
set(MPY_CXX "${MPY_CXX_PATH}")
message(STATUS "  native C++ compiler: ${MPY_CXX}")

string(REGEX REPLACE "g\\+\\+$" "objcopy" MPY_OBJCOPY_CANDIDATE "${MPY_CXX}")
find_program(MPY_OBJCOPY_PATH
    NAMES "${MPY_OBJCOPY_CANDIDATE}" xtensa-esp32s3-elf-objcopy xtensa-esp32s2-elf-objcopy xtensa-esp32-elf-objcopy objcopy
)
if(NOT MPY_OBJCOPY_PATH)
    message(FATAL_ERROR "objcopy not found for MPY_TARGET=${MPY_TARGET}")
endif()
set(MPY_OBJCOPY "${MPY_OBJCOPY_PATH}")
message(STATUS "  native objcopy: ${MPY_OBJCOPY}")

string(TOUPPER "${MPY_FLOAT_IMPL}" MPY_FLOAT_IMPL_UPPER)

set(NATIVE_ENTRY_SRC "${CMAKE_CURRENT_LIST_DIR}/native/ROSMicroPy.c")
set(NATIVE_COMPAT_SRC "${CMAKE_CURRENT_LIST_DIR}/native/native_mpy_compat.c")
set(ROSMICROPY_SRC
    "${ROSMICROPY_DIR}/mp_uros_modules/uros_mesg_func.c"
    "${ROSMICROPY_DIR}/mp_uros_modules/uros_base_func.c"
    "${ROSMICROPY_DIR}/mp_uros_modules/mp_obj_tools.c"
    "${ROSMICROPY_DIR}/mp_uros_modules/mp_uros_thread.c"
    "${ROSMICROPY_DIR}/mp_uros_type_support/mp_uros_type_support.c"
    "${ROSMICROPY_DIR}/mp_uros_type_support/mp_uros_dataTypeParser.c"
)
set(MP_HELPERS_SRC
    "${MP_HELPERS_DIR}/mp_helpers.cpp"
)
set(MICROROS_COMPONENT_SRC
    "${NATMOD_MICROROS_DIR}/network_interfaces/uros_wlan_netif.c"
    "${NATMOD_MICROROS_DIR}/network_interfaces/uros_ethernet_netif.c"
)
set(NATIVE_SRC
    ${NATIVE_ENTRY_SRC}
    ${NATIVE_COMPAT_SRC}
    ${ROSMICROPY_SRC}
    ${MP_HELPERS_SRC}
    ${MICROROS_COMPONENT_SRC}
)

set(CONFIG_H "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.config.h")
set(COMBINED_OBJ "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.combined.o")
set(NORMALIZED_OBJ "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.normalized.o")
set(NATIVE_MPY "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.native.mpy")
set(OUTPUT_MPY "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.mpy")

set(NATIVE_OBJ)
foreach(src ${NATIVE_SRC})
    file(RELATIVE_PATH rel_src "${CMAKE_CURRENT_LIST_DIR}" "${src}")
    string(MAKE_C_IDENTIFIER "${rel_src}" obj_name)
    list(APPEND NATIVE_OBJ "${CMAKE_CURRENT_BINARY_DIR}/${obj_name}.o")
endforeach()

set(IDF_INCLUDE_DIRS)
if(IDF_PATH AND EXISTS "${IDF_PATH}/components")
    set(IDF_INCLUDE_CANDIDATES
        "${IDF_PATH}/components/newlib/platform_include"
        "${IDF_PATH}/components/freertos/config/include"
        "${IDF_PATH}/components/freertos/config/include/freertos"
        "${IDF_PATH}/components/freertos/config/xtensa/include"
        "${IDF_PATH}/components/freertos/FreeRTOS-Kernel/include"
        "${IDF_PATH}/components/freertos/FreeRTOS-Kernel/portable/xtensa/include"
        "${IDF_PATH}/components/freertos/FreeRTOS-Kernel/portable/xtensa/include/freertos"
        "${IDF_PATH}/components/freertos/esp_additions/include"
        "${IDF_PATH}/components/esp_common/include"
        "${IDF_PATH}/components/esp_system/include"
        "${IDF_PATH}/components/esp_system/port/include"
        "${IDF_PATH}/components/esp_hw_support/include"
        "${IDF_PATH}/components/esp_hw_support/port/include"
        "${IDF_PATH}/components/esp_hw_support/port/${MPY_TARGET}/include"
        "${IDF_PATH}/components/hal/include"
        "${IDF_PATH}/components/hal/${MPY_TARGET}/include"
        "${IDF_PATH}/components/soc/include"
        "${IDF_PATH}/components/soc/${MPY_TARGET}/include"
        "${IDF_PATH}/components/soc/${MPY_TARGET}/register"
        "${IDF_PATH}/components/log/include"
        "${IDF_PATH}/components/heap/include"
        "${IDF_PATH}/components/esp_rom/include"
        "${IDF_PATH}/components/esp_rom/${MPY_TARGET}/include"
        "${IDF_PATH}/components/esp_netif/include"
        "${IDF_PATH}/components/esp_wifi/include"
        "${IDF_PATH}/components/esp_event/include"
        "${IDF_PATH}/components/esp_eth/include"
        "${IDF_PATH}/components/esp_driver_gpio/include"
        "${IDF_PATH}/components/esp_driver_spi/include"
        "${IDF_PATH}/components/esp_partition/include"
        "${IDF_PATH}/components/nvs_flash/include"
        "${IDF_PATH}/components/lwip/include"
        "${IDF_PATH}/components/lwip/port/include"
        "${IDF_PATH}/components/lwip/port/freertos/include"
        "${IDF_PATH}/components/lwip/port/esp32xx/include"
        "${IDF_PATH}/components/lwip/lwip/src/include"
        "${IDF_PATH}/components/pthread/include"
        "${IDF_PATH}/components/xtensa/include"
        "${IDF_PATH}/components/xtensa/${MPY_TARGET}/include"
    )
    foreach(include_dir ${IDF_INCLUDE_CANDIDATES})
        if(IS_DIRECTORY "${include_dir}")
            list(APPEND IDF_INCLUDE_DIRS "-I${include_dir}")
        endif()
    endforeach()
endif()

if(NOT EXISTS "${MICROROS_INCLUDE_DIR}/rcl/rcl.h" AND NOT EXISTS "${MICROROS_INCLUDE_DIR}/rcl/rcl/rcl.h")
    message(FATAL_ERROR
        "Generated micro-ROS headers were not found at ${MICROROS_INCLUDE_DIR}. "
        "Build or prepare natmod/micro_ros_espidf_component first so it creates "
        "rcl headers and libmicroros.a, or pass -DMICROROS_INCLUDE_DIR=/path/to/include."
    )
endif()
if(NOT EXISTS "${MICROROS_LIB}")
    message(FATAL_ERROR
        "Generated micro-ROS library was not found at ${MICROROS_LIB}. "
        "Build or prepare natmod/micro_ros_espidf_component first, or pass "
        "-DMICROROS_LIB=/path/to/libmicroros.a."
    )
endif()

set(MICROROS_INCLUDE_DIRS "-I${MICROROS_INCLUDE_DIR}")
file(GLOB MICROROS_PACKAGE_INCLUDE_CANDIDATES LIST_DIRECTORIES true "${MICROROS_INCLUDE_DIR}/*")
foreach(include_dir ${MICROROS_PACKAGE_INCLUDE_CANDIDATES})
    if(IS_DIRECTORY "${include_dir}")
        list(APPEND MICROROS_INCLUDE_DIRS "-I${include_dir}")
    endif()
endforeach()

set(MPY_CFLAGS
    -I${CMAKE_CURRENT_LIST_DIR}/native
    -I${CMAKE_CURRENT_BINARY_DIR}
    -I${MPY_DIR}
    -I${MPY_DIR}/ports/esp32
    -I${ROSMICROPY_DIR}/mp_uros_modules
    -I${ROSMICROPY_DIR}/mp_uros_type_support
    -I${MP_HELPERS_DIR}
    -I${NATMOD_MICROROS_DIR}/include_override
    -I${NATMOD_MICROROS_DIR}/network_interfaces
    ${MICROROS_INCLUDE_DIRS}
    ${IDF_INCLUDE_DIRS}
    -std=gnu11
    -Os
    -Wall
    -Werror
    -DNDEBUG
    -DNO_QSTR
    -DMICROPY_ENABLE_DYNRUNTIME
    -DMICROPY_PY_THREAD=1
    -DMICROPY_PY_THREAD_GIL=1
    "-DMP_CONFIGFILE=<${CONFIG_H}>"
    -DMICROPY_FLOAT_IMPL=MICROPY_FLOAT_IMPL_${MPY_FLOAT_IMPL_UPPER}
    -DCONFIG_IDF_TARGET_ESP32S3=1
    -DCONFIG_MICRO_ROS_ESP_XRCE_DDS_MIDDLEWARE=1
    -fpic
    -fno-common
    -U_FORTIFY_SOURCE
)
set(MPY_CXXFLAGS
    ${MPY_CFLAGS}
    -std=gnu++11
    -fno-rtti
    -fno-exceptions
)
list(REMOVE_ITEM MPY_CXXFLAGS -std=gnu11)

add_custom_command(
    OUTPUT "${CONFIG_H}"
    COMMAND "${CMAKE_COMMAND}" -E env "PYTHONPATH=${MPY_TOOL_PYTHONPATH}" "${Python3_EXECUTABLE}" "${MPY_LD}" --arch "${MPY_ARCH}" --preprocess -o "${CONFIG_H}" ${NATIVE_SRC}
    DEPENDS "${NATIVE_SRC}" "${MPY_LD}"
    COMMENT "Generating native .mpy qstr config"
    VERBATIM
)

foreach(src obj IN ZIP_LISTS NATIVE_SRC NATIVE_OBJ)
    get_filename_component(src_ext "${src}" EXT)
    if(src_ext STREQUAL ".cpp")
        add_custom_command(
            OUTPUT "${obj}"
            COMMAND "${MPY_CXX}" ${MPY_ARCH_FLAGS} ${MPY_CXXFLAGS} -o "${obj}" -c "${src}"
            DEPENDS "${src}" "${CONFIG_H}"
            COMMENT "Compiling ${src}"
            VERBATIM
        )
    else()
        add_custom_command(
            OUTPUT "${obj}"
            COMMAND "${MPY_CC}" ${MPY_ARCH_FLAGS} ${MPY_CFLAGS} -o "${obj}" -c "${src}"
            DEPENDS "${src}" "${CONFIG_H}"
            COMMENT "Compiling ${src}"
            VERBATIM
        )
    endif()
endforeach()

add_custom_command(
    OUTPUT "${COMBINED_OBJ}"
    COMMAND "${MPY_CXX}" ${MPY_ARCH_FLAGS} -r -o "${COMBINED_OBJ}" ${NATIVE_OBJ} "${MICROROS_LIB}"
    DEPENDS "${NATIVE_OBJ}" "${MICROROS_LIB}"
    COMMENT "Combining ROSMicroPy objects with libmicroros"
    VERBATIM
)

add_custom_command(
    OUTPUT "${NORMALIZED_OBJ}"
    COMMAND "${CMAKE_COMMAND}" -E copy "${COMBINED_OBJ}" "${NORMALIZED_OBJ}"
    COMMAND "${MPY_OBJCOPY}"
        --rename-section .data.default_allocator=.rodata.default_allocator,alloc,load,readonly,data
        --rename-section .data.goal_event_descriptions=.rodata.goal_event_descriptions,alloc,load,readonly,data
        --rename-section .data.goal_state_descriptions=.rodata.goal_state_descriptions,alloc,load,readonly,data
        "${NORMALIZED_OBJ}"
    DEPENDS "${COMBINED_OBJ}"
    COMMENT "Normalizing read-only micro-ROS data for native .mpy"
    VERBATIM
)

set(MPY_LD_EXTERNS)
if(MPY_EXTERNS_FILE)
    if(NOT EXISTS "${MPY_EXTERNS_FILE}")
        message(FATAL_ERROR "MPY_EXTERNS_FILE=${MPY_EXTERNS_FILE} does not exist")
    endif()
    list(APPEND MPY_LD_EXTERNS --externs "${MPY_EXTERNS_FILE}")
    message(STATUS "  native externs: ${MPY_EXTERNS_FILE}")
endif()

add_custom_command(
    OUTPUT "${NATIVE_MPY}"
    COMMAND "${CMAKE_COMMAND}" -E env "PYTHONPATH=${MPY_TOOL_PYTHONPATH}" "${Python3_EXECUTABLE}" "${MPY_LD}" --arch "${MPY_ARCH}" --qstrs "${CONFIG_H}" ${MPY_LD_EXTERNS} -o "${NATIVE_MPY}" "${NORMALIZED_OBJ}"
    DEPENDS "${NORMALIZED_OBJ}" "${CONFIG_H}" "${MPY_LD}"
    COMMENT "Linking native .mpy payload"
    VERBATIM
)

add_custom_command(
    OUTPUT "${OUTPUT_MPY}"
    COMMAND "${Python3_EXECUTABLE}" "${MPY_TOOL}" --merge -o "${OUTPUT_MPY}" "${NATIVE_MPY}"
    DEPENDS "${NATIVE_MPY}" "${MPY_TOOL}"
    COMMENT "Writing ${OUTPUT_MPY}"
    VERBATIM
)

add_custom_target(native_mpy ALL DEPENDS "${OUTPUT_MPY}")

install(FILES "${OUTPUT_MPY}" DESTINATION .)
