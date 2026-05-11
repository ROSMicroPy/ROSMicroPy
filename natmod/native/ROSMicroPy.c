#include "py/dynruntime.h"

#define STATIC_ONLY_MESSAGE \
    "ROSMicroPy's current libROSMicroPy sources are ESP-IDF User C Module " \
    "sources. They must be ported from MP_REGISTER_MODULE/py/runtime.h to " \
    "py/dynruntime.h before the full micro-ROS API can run from a native .mpy."

static const char component_report_text[] =
    "natmod evaluation:\n"
    "- libROSMicroPy: contains the MicroPython-facing ROS bindings, but is "
    "currently a firmware User C Module that depends on ESP-IDF, FreeRTOS, "
    "and micro-ROS symbols.\n"
    "- micropython-helpers: helper routines for MicroPython object parsing; "
    "currently C++ and std::stringstream based, which is not suitable for "
    "MicroPython dynamic native module linking without a C rewrite.\n"
    "- micro_ros_espidf_component: required ESP-IDF/micro-ROS dependency; "
    "the natmod directory copy is empty in this checkout, while the populated "
    "submodule lives under components/micro_ros_espidf_component.\n";

mp_obj_t component_report(void) {
    return mp_obj_new_str(component_report_text, sizeof(component_report_text) - 1);
}

mp_obj_t native_available(void) {
    return mp_const_false;
}

mp_obj_t init_ROS_Stack(void) {
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t run_ROS_Stack(void) {
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t setDomainID(mp_obj_t value) {
    (void)value;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t setNamespace(mp_obj_t value) {
    (void)value;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t setNodeName(mp_obj_t value) {
    (void)value;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t setAgentPort(mp_obj_t value) {
    (void)value;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t setAgentIP(mp_obj_t value) {
    (void)value;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t registerDataType(mp_obj_t value) {
    (void)value;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t dumpDataType(mp_obj_t value) {
    (void)value;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t publishMsg(mp_obj_t topic, mp_obj_t msg) {
    (void)topic;
    (void)msg;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t registerROSPublisher(mp_obj_t topic, mp_obj_t msg_type) {
    (void)topic;
    (void)msg_type;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t registerEventSubscription(mp_obj_t event_name, mp_obj_t event_type, mp_obj_t callback) {
    (void)event_name;
    (void)event_type;
    (void)callback;
    mp_raise_NotImplementedError(STATIC_ONLY_MESSAGE);
}

mp_obj_t mpy_init(mp_obj_fun_bc_t *self, size_t n_args, size_t n_kw, mp_obj_t *args) {
    (void)n_args;
    (void)n_kw;
    (void)args;

    MP_DYNRUNTIME_INIT_ENTRY

    mp_store_global(MP_QSTR_component_report, MP_DYNRUNTIME_MAKE_FUNCTION(component_report));
    mp_store_global(MP_QSTR_native_available, MP_DYNRUNTIME_MAKE_FUNCTION(native_available));
    mp_store_global(MP_QSTR_init_ROS_Stack, MP_DYNRUNTIME_MAKE_FUNCTION(init_ROS_Stack));
    mp_store_global(MP_QSTR_run_ROS_Stack, MP_DYNRUNTIME_MAKE_FUNCTION(run_ROS_Stack));
    mp_store_global(MP_QSTR_setDomainID, MP_DYNRUNTIME_MAKE_FUNCTION(setDomainID));
    mp_store_global(MP_QSTR_setNamespace, MP_DYNRUNTIME_MAKE_FUNCTION(setNamespace));
    mp_store_global(MP_QSTR_setNodeName, MP_DYNRUNTIME_MAKE_FUNCTION(setNodeName));
    mp_store_global(MP_QSTR_setAgentPort, MP_DYNRUNTIME_MAKE_FUNCTION(setAgentPort));
    mp_store_global(MP_QSTR_setAgentIP, MP_DYNRUNTIME_MAKE_FUNCTION(setAgentIP));
    mp_store_global(MP_QSTR_registerDataType, MP_DYNRUNTIME_MAKE_FUNCTION(registerDataType));
    mp_store_global(MP_QSTR_dumpDataType, MP_DYNRUNTIME_MAKE_FUNCTION(dumpDataType));
    mp_store_global(MP_QSTR_publishMsg, MP_DYNRUNTIME_MAKE_FUNCTION(publishMsg));
    mp_store_global(MP_QSTR_registerROSPublisher, MP_DYNRUNTIME_MAKE_FUNCTION(registerROSPublisher));
    mp_store_global(MP_QSTR_registerEventSubscription, MP_DYNRUNTIME_MAKE_FUNCTION(registerEventSubscription));

    MP_DYNRUNTIME_INIT_EXIT
}
