# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_rcl_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED rcl_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(rcl_FOUND FALSE)
  elseif(NOT rcl_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(rcl_FOUND FALSE)
  endif()
  return()
endif()
set(_rcl_CONFIG_INCLUDED TRUE)

# output package information
if(NOT rcl_FIND_QUIETLY)
  message(STATUS "Found rcl: 5.3.7 (${rcl_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'rcl' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${rcl_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(rcl_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "rcl-extras.cmake;ament_cmake_export_include_directories-extras.cmake;ament_cmake_export_libraries-extras.cmake;ament_cmake_export_targets-extras.cmake;ament_cmake_export_dependencies-extras.cmake")
foreach(_extra ${_extras})
  include("${rcl_DIR}/${_extra}")
endforeach()
