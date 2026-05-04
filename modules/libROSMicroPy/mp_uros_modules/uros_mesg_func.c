
#include "mp_uros_sdk.h"
#include "uros_base_func.h"
#include "uros_mesg_func.h"
#include "mp_uros_type_support.h"
#include "mp_obj_tools.h"
#include "mp_uros_dataTypeParser.h"

#include "py/runtime.h"
#include "py/obj.h"

#include "rcl/rcl.h"
#include "rcl/error_handling.h"
#include "rclc/rclc.h"
#include "rclc/executor.h"

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_microxrcedds_c/identifier.h"
#include "rosidl_typesupport_microxrcedds_c/message_type_support.h"
#include "mp_uros_type_support_visibility_control.h"

#include "esp_netif.h"
#include "esp_wifi.h"
//#include "uros_network_interfaces.h"



// MicroPython runs as a task under FreeRTOS
#define MP_TASK_PRIORITY (ESP_TASK_PRIO_MIN + 1)
#define MP_TASK_STACK_SIZE (16 * 1024)

#if CONFIG_IDF_TARGET_ESP32C3
#define MP_TASK_STACK_LIMIT_MARGIN (2048)
#else
#define MP_TASK_STACK_LIMIT_MARGIN (1024)
#endif

#define             ros_subscription_slots 10
ros_subscription    *g_ros_subscriptions;

#define             ros_publisher_slots 10
ros_publisher_t    *g_ros_publishers;


/***********************************************************************************************/
/***********************************************************************************************/
/***********************************************************************************************/



/**
 *
 * Create a new Subscription
 * eventName = Topic Name
 * eventType = the type strcture that defines the message that will be received.
 *  The EventType is the name of the type returned when registering the type.
 * eventCallback = the callback function that will be called when a message is received. 
 */
mp_obj_t registerEventSubscription(
    mp_obj_t eventName,
    mp_obj_t eventType,
    mp_obj_t eventCallback) {

    int cnt = ros_subscription_slots;

    // Input validation
    if (&mp_type_str != mp_obj_get_type(eventType)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Event type must be of type str"));
        return mp_const_none;
    }

    const char* cstr_eventType = mp_obj_str_get_str(eventType);
    if ((cstr_eventType == NULL) || strlen(cstr_eventType) == 0) {
        mp_raise_ValueError(MP_ERROR_TEXT("Event type can not be an null / empty string"));
        return mp_const_none;
	}

    // Look up the Type registration by Name, if there is no entry
    // then the type has not been registered.
    dxc_cb_t* type_CtrlBlk = findTypeByName(cstr_eventType);

    if (type_CtrlBlk == NULL) {
        mp_raise_ValueError(MP_ERROR_TEXT("You must first register type before registering for the Event Subscription"));
        return mp_const_none;
    }

    if (&mp_type_str != mp_obj_get_type(eventName)) {
        mp_raise_ValueError(MP_ERROR_TEXT("eventName is not a String"));
        return mp_const_none;
    }

    const char* cstr_eventName = mp_obj_str_get_str(eventName);
    if ((cstr_eventName == NULL) || strlen(cstr_eventName)==0) {
        mp_raise_ValueError(MP_ERROR_TEXT("Event name can not be an null / empty string"));
        return mp_const_none;
    }

    //
    // Find first available subscription slot.
    //
    for (int x = 0; x < cnt; x++)
    {
        if (g_ros_subscriptions[x].inUse == false)
        {
            g_ros_subscriptions[x].eventName = strdup(cstr_eventName);
            g_ros_subscriptions[x].mpEventCallback = eventCallback;
            g_ros_subscriptions[x].dataTypeCtrlBlk = type_CtrlBlk;

            g_ros_subscriptions[x].inUse = true;
            g_ros_subscriptions[x].resp = malloc(1000); //  malloc(rti.sizeResp);
            add_ROS_Service_Listener(&g_ros_subscriptions[x]);
            return eventName;
        }

    }

    mp_raise_ValueError(MP_ERROR_TEXT("No Available Subscriptions Slots"));
    return mp_const_none;
}


/**
 * 
 * 
 * 
*/
ros_subscription * get_ROS_Subscription(int slot) {
    
    if (slot >= ros_subscription_slots) return NULL;
    return &g_ros_subscriptions[slot];
}

/**
 *
 *
 */
void init_ROS_Subscriptions() {
    g_ros_subscriptions = malloc( (sizeof(ros_subscription) + 4) * ros_subscription_slots);

    for (int x=0; x<ros_subscription_slots; x++) {
        g_ros_subscriptions[x].inUse = false;
    };
}



/***
 * 
 * 
 * 
*/
void add_ROS_Service_Listener(ros_subscription* sub) {


	printf("Init Subscription Name=%s\r\n", sub->eventName);
	RCSOFTCHECK(rclc_subscription_init_default(
	 	&sub->rcl_service_subscription,
		&rmp_rcl_node,
		sub->dataTypeCtrlBlk->ros_mesg_type_support,
		sub->eventName);
	);
	
	RCSOFTCHECK(rclc_executor_add_subscription_with_context(
		&rmp_rclc_executor,
		&sub->rcl_service_subscription,
		sub->resp,
		&service_callback, 
		sub,
		ON_NEW_DATA));

}



/**
 *
 *
 *
 */
void service_callback(const void *response, void *context) {
    printf("in Service callback\r\n");

    const void **mp_data = response;
    ros_subscription* ros_sub = (ros_subscription *)context;

    MP_THREAD_GIL_ENTER();
    // mp_obj_t data = createObjFromThread();
    mp_call_function_1(ros_sub->mpEventCallback, *mp_data);
    MP_THREAD_GIL_EXIT();
}



/**
 *
 *
 */
void init_ROS_Publishers() {
    g_ros_publishers = malloc( (sizeof(ros_publisher_t) + 4) * ros_publisher_slots);

    for (int x=0; x<ros_publisher_slots; x++) {
        g_ros_publishers[x].inUse = false;
    };
}


ros_publisher_t* getPublisherByTopic(const char *topic) {

    for (int x = 0; x < ros_publisher_slots; x++)
    {
        if (g_ros_publishers[x].inUse == false) return NULL;
        
        if (strcmp(g_ros_publishers[x].topicName, topic) == 0) return &g_ros_publishers[x];
    }

    return NULL;

}

/**
 * 
 * 
 * 
*/
mp_obj_t  registerROSPublisher(
    mp_obj_t topicName,
    mp_obj_t dataType) {

    if (&mp_type_str != mp_obj_get_type(topicName)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Topic Name must be of type str"));
        return mp_const_none;
    }

    const char* cstr_topicName = mp_obj_str_get_str(topicName);
    if ((cstr_topicName == NULL) || strlen(cstr_topicName) == 0) {
        mp_raise_ValueError(MP_ERROR_TEXT("Topic name can not be an null / empty string"));
        return mp_const_none;
	}

    if (getPublisherByTopic(cstr_topicName) != NULL) {
        mp_raise_ValueError(MP_ERROR_TEXT("Topic name is already registered"));
        return mp_const_none;
    }

    if (&mp_type_str != mp_obj_get_type(dataType)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Data type must be of type str"));
        return mp_const_none;
    }

    const char* cstr_dataType = mp_obj_str_get_str(dataType);
    if ((cstr_dataType == NULL) || strlen(cstr_dataType) == 0) {
        mp_raise_ValueError(MP_ERROR_TEXT("Data type can not be an null / empty string"));
        return mp_const_none;
	}

    dxc_cb_t* type_CtrlBlk = findTypeByName(cstr_dataType);

    if (type_CtrlBlk == NULL) {
        mp_raise_ValueError(MP_ERROR_TEXT("You must first register type before registering for the Event Subscription"));
        return mp_const_none;
    }


    // Find first available subscription slot.
    //

    for (int x = 0; x < ros_publisher_slots; x++)
    {
        if (g_ros_publishers[x].inUse == false)
        {
            g_ros_publishers[x].topicName = cstr_topicName;
            g_ros_publishers[x].inUse = true;
            g_ros_publishers[x].dataTypeCtrlBlk = type_CtrlBlk;

            // create publisher
	        RCCHECK(rclc_publisher_init_default(
		        &g_ros_publishers[x].pub,
		        &rmp_rcl_node,
                g_ros_publishers[x].dataTypeCtrlBlk->ros_mesg_type_support,
		        (const char *)cstr_topicName));

            return topicName;
        }
    }

    mp_raise_ValueError(MP_ERROR_TEXT("No Available Publisher Slots"));
    return(mp_const_none);
}

/**
 * 
 * 
 */
 mp_obj_t publishMsg(mp_obj_t topicName, mp_obj_t data)
{		
//    printf("In Publish Mesg\r\n");
    if (&mp_type_str != mp_obj_get_type(topicName)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Topic Name must be of type str"));
        return mp_const_none;
    }

    const char* cstr_topicName = mp_obj_str_get_str(topicName);
    if ((cstr_topicName == NULL) || strlen(cstr_topicName) == 0) {
        mp_raise_ValueError(MP_ERROR_TEXT("Topic name can not be an null / empty string"));
        return mp_const_none;
	}

    ros_publisher_t* pub = getPublisherByTopic(cstr_topicName);

    if (pub == NULL) {
        mp_raise_ValueError(MP_ERROR_TEXT("Topic name is not registered"));
        return mp_const_none;
    }

    RCSOFTCHECK(rcl_publish(&pub->pub, data, NULL));

    return topicName;
}
