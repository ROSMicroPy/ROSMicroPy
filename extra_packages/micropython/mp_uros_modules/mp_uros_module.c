#include "mp_uros_module.h"
#include "mp_uros_thread.h"
#include "mp_uros.h"
#include "ros_app.h"

mp_obj_t registerEventSubscription(
    mp_obj_t eventName, mp_obj_t eventType, mp_obj_t eventCallback);

STATIC MP_DEFINE_CONST_FUN_OBJ_0(mp_init_ROS_Stack_obj, mp_init_ROS_Stack);
STATIC MP_DEFINE_CONST_FUN_OBJ_0(mp_run_ROS_Stack_obj, mp_run_ROS_Stack);

STATIC MP_DEFINE_CONST_FUN_OBJ_3(publishMsg_obj, publishMsg);
STATIC MP_DEFINE_CONST_FUN_OBJ_3(registerEventSubscription_obj, registerEventSubscription);

STATIC const mp_rom_map_elem_t mp_uros_module_globals_table[] = {
    {MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_microros)},

    {MP_ROM_QSTR(MP_QSTR_publishMsg), MP_ROM_PTR(&publishMsg_obj)},
    {MP_ROM_QSTR(MP_QSTR_registerEventSubscription), MP_ROM_PTR(&registerEventSubscription_obj)},
    {MP_ROM_QSTR(MP_QSTR_mp_init_ROS_Stack), MP_ROM_PTR(&mp_init_ROS_Stack_obj)},
    {MP_ROM_QSTR(MP_QSTR_mp_run_ROS_Stack), MP_ROM_PTR(&mp_run_ROS_Stack_obj)}

};

STATIC MP_DEFINE_CONST_DICT(mp_uros_module_globals, mp_uros_module_globals_table);

// Define module object.
const mp_obj_module_t mp_uros_user_cmodule = {
    .base = {&mp_type_module},
    .globals = (mp_obj_dict_t *)&mp_uros_module_globals,
};

// Register the module to make it available in Python.
MP_REGISTER_MODULE(MP_QSTR_microros, mp_uros_user_cmodule);
