# Create an INTERFACE library for our C module.
add_library(libROSMicroPy INTERFACE)
add_dependencies(libROSMicroPy  micro_ros_espidf_component)

get_filename_component(MICROROS_INC_DIR ../../../../components/micro_ros_espidf_component/include/include ABSOLUTE)
message("MicroRos ${MICROROS_INC_DIR}")

get_filename_component(ROS_MICROPY_DIR ../../../../modules/libROSMicroPy ABSOLUTE)
message("ROS Micropython ${ROS_MICROPY_DIR}")

get_filename_component(MICROPY_UROS_MODULE_DIR ${ROS_MICROPY_DIR}/mp_uros_modules ABSOLUTE)
get_filename_component(MICROPY_UROS_TYPE_SUPPORT_DIR ${ROS_MICROPY_DIR}/mp_uros_type_support ABSOLUTE)

set(ROS_MICROPY_MODULES
    #
    # Bind Python to ROS
    ${MICROPY_UROS_MODULE_DIR}/uros_mesg_func.c
    ${MICROPY_UROS_MODULE_DIR}/uros_base_func.c

    ${MICROPY_UROS_MODULE_DIR}/mp_uros_thread.c
    ${MICROPY_UROS_MODULE_DIR}/uros_mp_reg.c

    ${MICROPY_UROS_TYPE_SUPPORT_DIR}/mp_uros_type_support.c
    ${MICROPY_UROS_TYPE_SUPPORT_DIR}/mp_uros_dataTypeParser.c
    ${MICROPY_UROS_TYPE_SUPPORT_DIR}/mp_uros_type_support.c

)

set(ROS_MICROPY_INC_DIRS
    ${MICROROS_INC_DIR}
    ${MICROROS_INC_DIR}/rcl_action
    ${MICROROS_INC_DIR}/action_msgs
    ${MICROROS_INC_DIR}/unique_identifier_msgs
    ${MICROROS_INC_DIR}/builtin_interfaces
    ${MICROROS_INC_DIR}/rcl
    ${MICROROS_INC_DIR}/rcutils
    ${MICROROS_INC_DIR}/rmw
    ${MICROROS_INC_DIR}/rosidl_runtime_c
    ${MICROROS_INC_DIR}/rosidl_typesupport_interface
    ${MICROROS_INC_DIR}/type_description_interfaces
    ${MICROROS_INC_DIR}/service_msgs
    ${MICROROS_INC_DIR}/rosidl_dynamic_typesupport
    ${ROS_MICROPY_DIR}/mp_uros_modules
    ${ROS_MICROPY_DIR}/mp_uros_type_support
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

