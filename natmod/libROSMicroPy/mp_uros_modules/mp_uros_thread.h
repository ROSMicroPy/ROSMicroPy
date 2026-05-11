#ifndef __MP_UROS_THREAD_H__
#define __MP_UROS_THREAD_H__

#include <stdio.h>
#include <string.h>

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"

#include "py/stackctrl.h"
#include "py/mpthread.h"
#include "py/runtime.h"
#include "py/mpconfig.h"

#include "sdkconfig.h"

#include "mp_uros_sdk.h"


typedef struct _ros_thread_entry_args_t
{
    mp_obj_dict_t *dict_locals;
    mp_obj_dict_t *dict_globals;
    size_t stack_size;
    void (*fun_ptr)();
    size_t n_args;
    size_t n_kw;
    mp_obj_t args[];
} ros_thread_entry_args_t;



mp_obj_t start_new_ROS_thread(void (*entry_point_fun)());
void *ros_thread_entry(void *args_in);


#endif
