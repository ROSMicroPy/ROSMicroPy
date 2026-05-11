#ifndef __uros_mesg_func_h__
#define __uros_mesg_func_h__

#include "mp_uros_sdk.h"

void init_ROS_Subscriptions();;

void add_ROS_Service_Listener(ros_subscription* sub);
void service_callback(const void *response, void *context);
ros_subscription * get_ROS_Subscription(int slot);



#endif