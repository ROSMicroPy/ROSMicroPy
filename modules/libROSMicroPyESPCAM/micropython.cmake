

# Create an INTERFACE library for our C module.
add_library(libROSMicroPyESPCAM INTERFACE)

add_dependencies(libROSMicroPyESPCAM  micro_ros_espidf_component espressif/esp32-camera)

get_filename_component(MICROROS_DIR ../../../../components/micro_ros_espidf_component ABSOLUTE)
get_filename_component(MICROROS_INC_DIR ../../../../components/micro_ros_espidf_component/include ABSOLUTE)

message("MicroRos ${MICROROS_INC_DIR}")
get_filename_component(ESP32_CAMERA_INC_DIR ../../../../components/espressif__esp32-camera/driver/include ABSOLUTE)

get_filename_component(ROS_MICROPY_ESPCAM_DIR ../../../../modules/libROSMicroPyESPCAM ABSOLUTE)
message("ESPCAMDIR = ${ROS_MICROPY_ESPCAM_DIR}")
message("CMAKE_CURRENT_LIST_DIR = ${CMAKE_CURRENT_LIST_DIR}")

set(RMP_SERVER_SRC 
    ${ROS_MICROPY_ESPCAM_DIR}/server/rmp_cam_server.c
)

set (RMP_PUBLISHER_SRC
    ${ROS_MICROPY_ESPCAM_DIR}/publisher/rmp_cam_publisher.c
)

set (ROS_MICROPY_ESPCAM_SRC
    ${ROS_MICROPY_ESPCAM_DIR}/rmp_cam_main.c
    ${ROS_MICROPY_ESPCAM_DIR}/rmp_cam_common.c
    ${RMP_PUBLISHER_SRC}
    #${RMP_SERVER_SRC}
)
message("ROS_MICROPY_ESPCAM_SRC = ${ROS_MICROPY_ESPCAM_SRC}")
message("IDF_PATH = $ENV{IDF_PATH}") # $IDF_PATH


set (ROS_MICROPY_ESPCAM_INC  
    ${ROS_MICROPY_ESPCAM_DIR}
    ${ROS_MICROPY_ESPCAM_DIR}/server
    ${MICROROS_INC_DIR}/std_msgs
    ${MICROROS_INC_DIR}/sensor_msgs
    ${MICROROS_INC_DIR}/example_interfaces   
    ${MICROROS_INC_DIR}/rosidl_typesupport_introspection_c
    ${ESP32_CAMERA_INC_DIR}
    ${CMAKE_CURRENT_LIST_DIR}../../../components/espressif__esp32-camera/conversions/include
    ${IDF_PATH}/components/json/cJSON
)

# Add our source files to the lib
target_sources(libROSMicroPyESPCAM INTERFACE
    ${ROS_MICROPY_ESPCAM_SRC}
)

# Add the current directory as an include directory.
target_include_directories(libROSMicroPyESPCAM INTERFACE
    ${ROS_MICROPY_ESPCAM_INC}
)

list(APPEND CMAKE_MODULE_PATH 
  ${MICROROS_DIR}/micro_ros_src/install/share/rosidl_default_generators/cmake/
  ${MICROROS_DIR}/micro_ros_dev/install/ament_cmake/share/ament_cmake/cmake/
  ${MICROROS_DIR}/micro_ros_dev/install/ament_cmake/share/ament_cmake
  ${MICROROS_DIR}/micro_ros_dev/install/ament_cmake_libraries/share/ament_cmake_libraries/cmake
)
message("CMake Module ${CMAKE_MODULE_PATH}")

# list( APPEND ament_cmake_libraries_DIR
#     ${MICROROS_DIR}/micro_ros_dev/install/ament_cmake_libraries/share/ament_cmake_libraries/cmake
# )

# list( APPEND ament_cmake_core_DIR 
#     ${MICROROS_DIR}/micro_ros_dev/install/ament_cmake_core/share/ament_cmake_core/cmake
# )

# list( APPEND ament_cmake_DIR
#     ${MICROROS_DIR}/micro_ros_dev/install/ament_cmake/share/ament_cmake/cmake/
# )

# message("Ament CMake ${ament_cmake_DIR}")

# find_package(ament_package REQUIRED)
# find_package(ament_cmake REQUIRED)
# find_package(rosidl_default_generators REQUIRED)
# rosidl_generate_interfaces(libROSMicroPyESPCAM
#     "interfaces/srv/Image.srv"
# )


#ament_export_dependencies(rosidl_default_runtime)
#ament_package()

# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE libROSMicroPyESPCAM)

