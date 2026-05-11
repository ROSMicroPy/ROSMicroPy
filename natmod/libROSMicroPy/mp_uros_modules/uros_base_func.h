#ifndef __UROS_BASE_FUNC_H__
#define __UROS_BASE_FUNC_H__

#include "py/runtime.h"
#include "py/obj.h"

#include "rcl/rcl.h"
#include "rcl/error_handling.h"
#include "rclc/rclc.h"
#include "rclc/executor.h"


void init_event_subscription_callbacks();
void init_ROS_Publishers();


#endif
