cmake_minimum_required(VERSION 3.16)

project(rosmicropy_native_mpy C)

set(MPY_DIR "${CMAKE_CURRENT_LIST_DIR}/../micropython" CACHE PATH "Path to the MicroPython source tree")
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

set(MPY_LD "${MPY_DIR}/tools/mpy_ld.py")
set(MPY_TOOL "${MPY_DIR}/tools/mpy-tool.py")
set(MPY_CROSS "${MPY_DIR}/mpy-cross/build/mpy-cross")

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
set(MPY_FLOAT_IMPL double)
set(MPY_ARCH_FLAGS -fno-stack-protector)

if(MPY_ARCH STREQUAL "x86")
    set(MPY_ARCH_FLAGS -m32 -fno-stack-protector)
elseif(MPY_ARCH STREQUAL "x64")
    set(MPY_ARCH_FLAGS -fno-stack-protector)
elseif(MPY_ARCH STREQUAL "armv6m")
    set(MPY_CC arm-none-eabi-gcc)
    set(MPY_ARCH_FLAGS -mthumb -mcpu=cortex-m0)
    set(MPY_FLOAT_IMPL none)
elseif(MPY_ARCH STREQUAL "armv7m")
    set(MPY_CC arm-none-eabi-gcc)
    set(MPY_ARCH_FLAGS -mthumb -mcpu=cortex-m3)
    set(MPY_FLOAT_IMPL none)
elseif(MPY_ARCH STREQUAL "armv7emsp")
    set(MPY_CC arm-none-eabi-gcc)
    set(MPY_ARCH_FLAGS -mthumb -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard)
    set(MPY_FLOAT_IMPL float)
elseif(MPY_ARCH STREQUAL "armv7emdp")
    set(MPY_CC arm-none-eabi-gcc)
    set(MPY_ARCH_FLAGS -mthumb -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard)
    set(MPY_FLOAT_IMPL double)
elseif(MPY_ARCH STREQUAL "xtensa")
    set(MPY_CC xtensa-lx106-elf-gcc)
    set(MPY_ARCH_FLAGS -mforce-l32)
    set(MPY_FLOAT_IMPL none)
elseif(MPY_ARCH STREQUAL "xtensawin")
    if(MPY_TARGET STREQUAL "esp32s3")
        set(MPY_CC xtensa-esp32s3-elf-gcc)
    elseif(MPY_TARGET STREQUAL "esp32s2")
        set(MPY_CC xtensa-esp32s2-elf-gcc)
    else()
        set(MPY_CC xtensa-esp32-elf-gcc)
    endif()
    set(MPY_ARCH_FLAGS)
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

string(TOUPPER "${MPY_FLOAT_IMPL}" MPY_FLOAT_IMPL_UPPER)

set(NATIVE_SRC "${CMAKE_CURRENT_LIST_DIR}/native/ROSMicroPy.c")
set(CONFIG_H "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.config.h")
set(NATIVE_OBJ "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.o")
set(NATIVE_MPY "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.native.mpy")
set(OUTPUT_MPY "${CMAKE_CURRENT_BINARY_DIR}/${MPY_MODULE_NAME}.mpy")

set(MPY_CFLAGS
    -I${CMAKE_CURRENT_LIST_DIR}/native
    -I${MPY_DIR}
    -std=c99
    -Os
    -Wall
    -Werror
    -DNDEBUG
    -DNO_QSTR
    -DMICROPY_ENABLE_DYNRUNTIME
    "-DMP_CONFIGFILE=<${CONFIG_H}>"
    -DMICROPY_FLOAT_IMPL=MICROPY_FLOAT_IMPL_${MPY_FLOAT_IMPL_UPPER}
    -fpic
    -fno-common
    -U_FORTIFY_SOURCE
)

add_custom_command(
    OUTPUT "${CONFIG_H}"
    COMMAND "${Python3_EXECUTABLE}" "${MPY_LD}" --arch "${MPY_ARCH}" --preprocess -o "${CONFIG_H}" "${NATIVE_SRC}"
    DEPENDS "${NATIVE_SRC}" "${MPY_LD}"
    COMMENT "Generating native .mpy qstr config"
    VERBATIM
)

add_custom_command(
    OUTPUT "${NATIVE_OBJ}"
    COMMAND "${MPY_CC}" ${MPY_ARCH_FLAGS} ${MPY_CFLAGS} -o "${NATIVE_OBJ}" -c "${NATIVE_SRC}"
    DEPENDS "${NATIVE_SRC}" "${CONFIG_H}"
    COMMENT "Compiling ${MPY_MODULE_NAME}.o for ${MPY_ARCH}"
    VERBATIM
)

add_custom_command(
    OUTPUT "${NATIVE_MPY}"
    COMMAND "${Python3_EXECUTABLE}" "${MPY_LD}" --arch "${MPY_ARCH}" --qstrs "${CONFIG_H}" -o "${NATIVE_MPY}" "${NATIVE_OBJ}"
    DEPENDS "${NATIVE_OBJ}" "${CONFIG_H}" "${MPY_LD}"
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
