#ifndef __MP_SDK_IMPL_H__
#define __MP_SDK_IMPL_H__

#include "rcl/rcl.h"
#include "rcl/error_handling.h"
#include "rclc/rclc.h"
#include "rclc/executor.h"

#include "py/runtime.h"

#define DEBUG 0

#if DEBUG
#define DEBUG_printf(...) ESP_LOGI("ros_mp_thread", __VA_ARGS__)
#else
#define DEBUG_printf(...) (void)0
#endif


#ifdef CONFIG_MICRO_ROS_ESP_XRCE_DDS_MIDDLEWARE
#include <rmw_microros/rmw_microros.h>
#endif


#define RCCHECK(fn)                                                                      \
	{                                                                                    \
		rcl_ret_t temp_rc = fn;                                                          \
		if ((temp_rc != RCL_RET_OK))                                                     \
		{                                                                                \
			printf("Failed status on line %d: %d. Aborting.\n", __LINE__, (int)temp_rc); \
			vTaskDelete(NULL);                                                           \
		}                                                                                \
	}

#define RCSOFTCHECK(fn)                                                                    \
	{                                                                                      \
		rcl_ret_t temp_rc = fn;                                                            \
		if ((temp_rc != RCL_RET_OK))                                                       \
		{                                                                                  \
			printf("Failed status on line %d: %d. Continuing.\n", __LINE__, (int)temp_rc); \
		}                                                                                  \
	}


typedef struct _ros_subscription
{
    int index;
    mp_obj_t eventName;
    mp_obj_t eventType;
    void *resp;
    mp_obj_t mpEventCallback;

    rcl_subscription_t rcl_service_subscription;

} ros_subscription;

ros_subscription* get_ROS_Sub_from_slot(int slot);

#define DOMAIN_ID 0

extern rclc_executor_t		executor;
extern rcl_node_t 			node;
extern rcl_timer_t			timer;
extern rcl_allocator_t		allocator;
extern rclc_support_t		support;
extern rcl_init_options_t   init_options;
extern rmw_init_options_t   *rmw_options;


void dispatch_ROSMsg();
void run_ROS_Stack();

mp_obj_t publishMsg(mp_obj_t publisher_ID, mp_obj_t dataType, mp_obj_t data);

mp_obj_t registerEventSubscription(
    mp_obj_t eventName,
    mp_obj_t eventType,
    mp_obj_t eventCallback);


mp_obj_t registerDataType(mp_obj_t name, mp_obj_t dataMap);

mp_obj_t	mp_run_ROS_Stack();
mp_obj_t	init_ROS_Stack();

mp_obj_t setDomainID(mp_obj_t id);
mp_obj_t setNamespace(mp_obj_t namespace);
mp_obj_t setNodeName(mp_obj_t name);
mp_obj_t setWifiConfig(mp_obj_t sta_id, mp_obj_t pass);

#endif