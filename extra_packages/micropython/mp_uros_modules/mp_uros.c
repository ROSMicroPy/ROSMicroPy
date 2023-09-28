#include "mp_uros.h"
#include "mp_uros_module.h"
#include "mp_uros_thread.h"
#include "ros_app.h"

// MicroPython runs as a task under FreeRTOS
#define MP_TASK_PRIORITY (ESP_TASK_PRIO_MIN + 1)
#define MP_TASK_STACK_SIZE (16 * 1024)

#if CONFIG_IDF_TARGET_ESP32C3
#define MP_TASK_STACK_LIMIT_MARGIN (2048)
#else
#define MP_TASK_STACK_LIMIT_MARGIN (1024)
#endif

int ros_subscription_slots = 10;
ros_subscription* g_ros_subs;

/***********************************************************************************************/
/***********************************************************************************************/
/***********************************************************************************************/
/***********************************************************************************************/
mp_obj_t publishMsg(mp_obj_t publisher_ID, mp_obj_t dataType, mp_obj_t data)
{
    return NULL;
}

/**
 *
 */
mp_obj_t createObjFromThread()
{

    mp_obj_t linear = mp_obj_new_dict(3);
    linear = mp_obj_dict_store(linear, mp_obj_new_str("x", 1), mp_obj_new_float(0x40));
    linear = mp_obj_dict_store(linear, mp_obj_new_str("y", 1), mp_obj_new_float(0x50));
    linear = mp_obj_dict_store(linear, mp_obj_new_str("z", 1), mp_obj_new_float(0x60));

    mp_obj_t angular = mp_obj_new_dict(3);
    angular = mp_obj_dict_store(angular, mp_obj_new_str("x", 1), mp_obj_new_float(0x70));
    angular = mp_obj_dict_store(angular, mp_obj_new_str("y", 1), mp_obj_new_float(0x80));
    angular = mp_obj_dict_store(angular, mp_obj_new_str("z", 1), mp_obj_new_float(0x90));

    mp_obj_t twist = mp_obj_new_dict(2);
    twist = mp_obj_dict_store(twist, mp_obj_new_str("linear", 6), linear);
    twist = mp_obj_dict_store(twist, mp_obj_new_str("angular", 7), angular);

    //    mp_store_global(MP_QSTR_make_dict, MP_OBJ_FROM_PTR(&make_dict_obj));

    return (twist);
}

/**
 *
 *
 *
 */
void service_callback(const void *res, void *context)
{
    printf("in Service callback\r\n");
    if (context == NULL)
        return;

    ros_subscription *ros_sub = (ros_subscription *)context;
    MP_THREAD_GIL_ENTER();
    mp_obj_t data = createObjFromThread();
    mp_call_function_1(ros_sub->mpEventCallback, data);
    MP_THREAD_GIL_EXIT();
}

/**
 *
 *
 */
void init_event_subscription_callbacks()
{
    g_ros_subs = malloc(sizeof(ros_subscription) * ros_subscription_slots);

    ros_subscription* rsubs = g_ros_subs;
    for (int x=0; x<ros_subscription_slots; x++) {
        rsubs->index=0;
        rsubs++;
    };
}

/**
 *
 *
 *
 */
mp_obj_t registerEventSubscription(
    mp_obj_t eventName,
    mp_obj_t eventType,
    mp_obj_t eventCallback)
{

 //   const char *ename = mp_obj_str_get_str(eventName);

    int cnt = ros_subscription_slots;
    ros_subscription* rsubs = g_ros_subs;

    for (int x = 0; x < cnt; x++)
    {
        if (rsubs->index == 0)
        {
            rsubs->eventName = eventName;
            rsubs->eventType = eventType;
            rsubs->mpEventCallback = eventCallback;

            rsubs->index = x;
            rsubs->resp = malloc(1000); //  malloc(rti.sizeResp);
            add_ROS_service_Listener(rsubs);
            return eventName;
        }

        rsubs++;
    }

    return mp_const_none;
}

/**
 *
 */
mp_obj_t mp_init_ROS_Stack()
{
    printf("\r\nInitializing ROS Stack\r\n");
    init_event_subscription_callbacks();
    init_ROS_Stack();

    return mp_const_none;
}

mp_obj_t mp_run_ROS_Stack()
{
    start_new_ROS_thread(run_ROS_Stack);
    return mp_const_none;
}
