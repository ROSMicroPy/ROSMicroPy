# Create an INTERFACE library for our C module.
add_library(libROSMicroPy INTERFACE)

get_filename_component(ROSMICROPY_COMPONENTS_DIR "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
get_filename_component(REPO_ROOT "${ROSMICROPY_COMPONENTS_DIR}/.." ABSOLUTE)

get_filename_component(MICROROS_COMPONENT_DIR "${ROSMICROPY_COMPONENTS_DIR}/micro_ros_espidf_component" ABSOLUTE)
get_filename_component(MICROROS_INC_DIR "${MICROROS_COMPONENT_DIR}/include" ABSOLUTE)
message("micro-ROS component ${MICROROS_COMPONENT_DIR}")
message("micro-ROS include ${MICROROS_INC_DIR}")

get_filename_component(ROS_MICROPY_DIR "${ROSMICROPY_COMPONENTS_DIR}/libROSMicroPy" ABSOLUTE)
message("ROSMicroPy ${ROS_MICROPY_DIR}")

get_filename_component(MICROPY_UROS_MODULE_DIR ${ROS_MICROPY_DIR}/mp_uros_modules ABSOLUTE)
get_filename_component(MICROPY_UROS_TYPE_SUPPORT_DIR ${ROS_MICROPY_DIR}/mp_uros_type_support ABSOLUTE)
get_filename_component(MICROPY_HELPERS_DIR "${ROSMICROPY_COMPONENTS_DIR}/micropython-helpers" ABSOLUTE)

set(ROS_MICROPY_MODULES
    #
    # Bind Python to ROS
    ${MICROPY_UROS_MODULE_DIR}/uros_mesg_func.c
    ${MICROPY_UROS_MODULE_DIR}/uros_base_func.c

    ${MICROPY_UROS_MODULE_DIR}/mp_obj_tools.c
    ${MICROPY_UROS_MODULE_DIR}/mp_uros_thread.c
    ${MICROPY_UROS_MODULE_DIR}/uros_mp_reg.c

    ${MICROPY_UROS_TYPE_SUPPORT_DIR}/mp_uros_type_support.c
    ${MICROPY_UROS_TYPE_SUPPORT_DIR}/mp_uros_dataTypeParser.c

)

list(APPEND MICROPY_FROZEN_MANIFEST
    ${ROS_MICROPY_DIR}/manifest.py
)

message("FROZEN CONTENT: ${MICROPY_FROZEN_MANIFEST}")
set(MICROROS_INC_DIRS ${MICROROS_INC_DIR})

file(GLOB MICROROS_PACKAGE_INCLUDE_CANDIDATES LIST_DIRECTORIES true "${MICROROS_INC_DIR}/*")
foreach(include_dir ${MICROROS_PACKAGE_INCLUDE_CANDIDATES})
    if(IS_DIRECTORY "${include_dir}")
        list(APPEND MICROROS_INC_DIRS "${include_dir}")
    endif()
endforeach()

set(ROS_MICROPY_INC_DIRS
    ${MICROROS_INC_DIRS}
    ${ROS_MICROPY_DIR}/mp_uros_modules
    ${ROS_MICROPY_DIR}/mp_uros_type_support
    ${MICROPY_HELPERS_DIR}
)

# Add our source files to the lib
target_sources(libROSMicroPy INTERFACE
    ${ROS_MICROPY_MODULES}
)

# Add the current directory as an include directory.
target_include_directories(libROSMicroPy INTERFACE
    ${ROS_MICROPY_INC_DIRS}
)

# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE libROSMicroPy)

if(TARGET micropython-helpers)
    target_link_libraries(libROSMicroPy INTERFACE micropython-helpers)
endif()

if(TARGET micro_ros_espidf_component)
    add_dependencies(libROSMicroPy micro_ros_espidf_component)
    target_link_libraries(usermod INTERFACE micro_ros_espidf_component)
endif()
