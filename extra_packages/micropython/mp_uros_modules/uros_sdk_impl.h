#ifndef __MP_SDK_IMPL_H__
#define __MP_SDK_IMPL_H__

#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/task.h"

#include "rcl/rcl.h"
#include "rcl/error_handling.h"
#include "rclc/rclc.h"
#include "rclc/executor.h"

#include "py/runtime.h"
#include "py/gc.h"
#include "mphalport.h"
#include "py/mpthread.h"
#include "py/mpconfig.h"
#include "py/stackctrl.h"

#include "shared/runtime/pyexec.h"

ros_subscription* get_ROS_Sub_from_slot(int slot);
void dispatch_ROSMsg();

void init_event_subscription_callbacks();
mp_obj_t publishMsg(mp_obj_t publisher_ID, mp_obj_t dataType, mp_obj_t data);
mp_obj_t registerEventSubscription(
    mp_obj_t eventName,
    mp_obj_t eventType,
    mp_obj_t eventCallback);


#endif