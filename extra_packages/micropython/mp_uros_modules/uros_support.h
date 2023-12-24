#ifndef __UROS_SUPPORT_H__
#define __UROS_SUPPORT_H__

#include "py/runtime.h"
#include "py/obj.h"

#include "rcl/rcl.h"
#include "rcl/error_handling.h"
#include "rclc/rclc.h"
#include "rclc/executor.h"

#ifdef CONFIG_MICRO_ROS_ESP_XRCE_DDS_MIDDLEWARE
#include <rmw_microros/rmw_microros.h>
#endif

#include "mp_uros_thread.h"
#include "mp_uros_type_support.h"

#include "uros_sdk_api.h"
#include "uros_sdk_impl.h"


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



#define DOMAIN_ID 0

extern rclc_executor_t		executor;
extern rcl_node_t 			node;
extern rcl_timer_t			timer;
extern rcl_allocator_t		allocator;
extern rclc_support_t		support;
extern rcl_init_options_t   init_options;
extern rmw_init_options_t   *rmw_options;

mp_obj_t init_ROS_Stack();
mp_obj_t run_ROS_Stack();

void add_ROS_service_Listener(ros_subscription* sub);
void service_callback(const void *response, void *context);

#endif