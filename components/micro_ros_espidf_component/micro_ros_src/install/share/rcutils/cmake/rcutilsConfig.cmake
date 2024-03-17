# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_rcutils_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED rcutils_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(rcutils_FOUND FALSE)
  elseif(NOT rcutils_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(rcutils_FOUND FALSE)
  endif()
  return()
endif()
set(_rcutils_CONFIG_INCLUDED TRUE)

# output package information
if(NOT rcutils_FIND_QUIETLY)
  message(STATUS "Found rcutils: 5.1.5 (${rcutils_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'rcutils' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${rcutils_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(rcutils_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "ament_cmake_export_include_directories-extras.cmake;ament_cmake_export_libraries-extras.cmake;ament_cmake_export_targets-extras.cmake;ament_cmake_export_dependencies-extras.cmake")
foreach(_extra ${_extras})
  include("${rcutils_DIR}/${_extra}")
endforeach()
