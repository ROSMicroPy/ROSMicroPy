
#include "mp_uros_thread.h"

#include "sdkconfig.h"

#include <rcl/rcl.h>
#include <rcl/error_handling.h>

#include <rclc/rclc.h>
#include <rclc/executor.h>

#ifdef CONFIG_MICRO_ROS_ESP_XRCE_DDS_MIDDLEWARE
#include <rmw_microros/rmw_microros.h>
#endif

#include "mp_uros_type_support__functions.h"
#include "uros_support.h"


STATIC void *ros_thread_entry(void *args_in)
{
    printf("\r\nStarting ROS Thread");

    // Execution begins here for a new thread.  We do not have the GIL.
    ros_thread_entry_args_t *args = (ros_thread_entry_args_t *)args_in;

    mp_state_thread_t ts;
    mp_thread_set_state(&ts);

    mp_stack_set_top(&ts + 1); // need to include ts in root-pointer scan
    mp_stack_set_limit(args->stack_size);

#if MICROPY_ENABLE_PYSTACK
    // TODO threading and pystack is not fully supported, for now just make a small stack
    mp_obj_t mini_pystack[128];
    mp_pystack_init(mini_pystack, &mini_pystack[128]);
#endif

    // The GC starts off unlocked on this thread.
    ts.gc_lock_depth = 0;

    ts.mp_pending_exception = MP_OBJ_NULL;

    // set locals and globals from the calling context
    mp_locals_set(args->dict_locals);
    mp_globals_set(args->dict_globals);


    MP_THREAD_GIL_ENTER();

    // signal that we are set up and running
    mp_thread_start();

    // TODO set more thread-specific state here:
    //  cur_exception (root pointer)
    MP_THREAD_GIL_EXIT();

    run_ROS_Stack();

    // signal that we are finished
    mp_thread_finish();

    return NULL;
}

mp_obj_t start_new_ROS_thread(void (*entry_point_fun)())
{   
    ros_thread_entry_args_t *th_args = malloc(sizeof(ros_thread_entry_args_t));

    // pass our locals and globals into the new thread
    th_args->dict_locals = mp_locals_get();
    th_args->dict_globals = mp_globals_get();

    // set the stack size to use
    th_args->stack_size = CONFIG_MICRO_ROS_APP_STACK;

    // set the function for thread entry
    th_args->fun_ptr = entry_point_fun;

    // spawn the thread!
    mp_thread_create(ros_thread_entry, th_args, &th_args->stack_size);

    return mp_const_none;
}



