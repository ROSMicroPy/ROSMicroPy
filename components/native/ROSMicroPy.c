#include "py/dynruntime.h"

extern mp_obj_t init_ROS_Stack(void);
extern mp_obj_t mp_run_ROS_Stack(void);
extern mp_obj_t setDomainID(mp_obj_t id);
extern mp_obj_t setNamespace(mp_obj_t name_space);
extern mp_obj_t setNodeName(mp_obj_t name);
extern mp_obj_t setAgentPort(mp_obj_t obj_in);
extern mp_obj_t setAgentIP(mp_obj_t obj_in);
extern mp_obj_t registerDataType(mp_obj_t data_map);
extern mp_obj_t dumpDataType(mp_obj_t data_type_name);
extern mp_obj_t publishMsg(mp_obj_t topic_name, mp_obj_t data);
extern mp_obj_t registerROSPublisher(mp_obj_t topic_name, mp_obj_t data_type);
extern mp_obj_t registerEventSubscription(
    mp_obj_t event_name,
    mp_obj_t event_type,
    mp_obj_t event_callback);

static const char component_report_text[] =
    "natmod implementation build:\n"
    "- libROSMicroPy implementation sources are compiled into this native module.\n"
    "- micropython-helpers is compiled into this native module.\n"
    "- micro_ros_espidf_component headers/network interface sources are part of "
    "the build inputs; generated micro-ROS headers must be present for the full "
    "build to compile and link.\n";

mp_obj_t component_report(void) {
    return mp_obj_new_str(component_report_text, sizeof(component_report_text) - 1);
}

mp_obj_t native_available(void) {
    return mp_const_true;
}

mp_obj_t mpy_init(mp_obj_fun_bc_t *self, size_t n_args, size_t n_kw, mp_obj_t *args) {
    (void)n_args;
    (void)n_kw;
    (void)args;

    MP_DYNRUNTIME_INIT_ENTRY

    mp_store_global(MP_QSTR_component_report, MP_DYNRUNTIME_MAKE_FUNCTION(component_report));
    mp_store_global(MP_QSTR_native_available, MP_DYNRUNTIME_MAKE_FUNCTION(native_available));
    mp_store_global(MP_QSTR_init_ROS_Stack, MP_DYNRUNTIME_MAKE_FUNCTION(init_ROS_Stack));
    mp_store_global(MP_QSTR_run_ROS_Stack, MP_DYNRUNTIME_MAKE_FUNCTION(mp_run_ROS_Stack));
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
