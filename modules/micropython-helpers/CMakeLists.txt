# Component directive
set(SOURCES "mp_helpers.c")
set(INCLUDES .
    ../../../micropython/
)
idf_component_register(
    SRCS ${SOURCES}
    INCLUDE_DIRS ${INCLUDES}
)
