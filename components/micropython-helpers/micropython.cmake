# Create an INTERFACE library for our C module.
add_library(micropython-helpers INTERFACE)


get_filename_component(MP_HELPERS_DIR "${CMAKE_CURRENT_LIST_DIR}" ABSOLUTE)

set (MP_HELPERS_SRC
    ${MP_HELPERS_DIR}/mp_helpers.cpp

)

set (MP_HELPERS_INC  
    ${MP_HELPERS_DIR}
)

# Add our source files to the lib
target_sources(micropython-helpers INTERFACE
    ${MP_HELPERS_SRC}
)

# Add the current directory as an include directory.
target_include_directories(micropython-helpers  INTERFACE
    ${MP_HELPERS_INC}
)

# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE micropython-helpers )
