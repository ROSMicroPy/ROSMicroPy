#include "sdkconfig.h"

#include "mp_uros_sdk.h"
#include "uros_base_func.h"

#include "mp_obj_tools.h"
#include "mp_uros_type_support.h"
#include "mp_uros_thread.h"
#include "mp_uros_dataTypeParser.h"
#include "uros_mesg_func.h"
#include "sdkconfig.h"

#include "esp_wifi.h"
#include "esp_netif.h"


rclc_executor_t		rmp_rclc_executor;
rcl_node_t 			rmp_rcl_node;
rcl_allocator_t		rmp_rcl_allocator;
rclc_support_t		rmp_rclc_support;
rcl_init_options_t  init_options;
rmw_init_options_t *rmw_options;

rcl_timer_t       	main_timer;

size_t				rmp_domain_id = DOMAIN_ID;
char				rmp_node_name[64] = "turtle2";
char				rmp_namespace[64] = "";


char				ROS_AgentIP[64] = "192.168.8.100"; //CONFIG_MICRO_ROS_AGENT_IP;
char				ROS_AgentPort[64] = "8888"; //CONFIG_MICRO_ROS_AGENT_PORT;


/** 
 * 
 * 
*/
mp_obj_t setAgentIP(mp_obj_t obj_in)
{
    if (&mp_type_str != mp_obj_get_type(obj_in)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Agent IP must be a str"));
		return obj_in;
    }

    const char* cstr = mp_obj_str_get_str(obj_in);
    if ((cstr == NULL) || strlen(cstr)==0) {
		mp_raise_ValueError(MP_ERROR_TEXT("AgentIP must be a string"));
		return obj_in;
    }

	strncpy(ROS_AgentIP, cstr, 63);
	return obj_in;
}

/** 
 * 
 * 
*/
mp_obj_t setAgentPort(mp_obj_t obj_in)
{
    if (&mp_type_str != mp_obj_get_type(obj_in)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Agent Port must be a str"));
		return obj_in;
    }

    const char* cstr = mp_obj_str_get_str(obj_in);
    if ((cstr == NULL) || strlen(cstr)==0) {
		mp_raise_ValueError(MP_ERROR_TEXT("Agent Port must be a string"));
		return obj_in;
    }

	strncpy(ROS_AgentPort, cstr, 63);
	return obj_in;
}



/**
 * 
 * 
*/
mp_obj_t setDomainID(mp_obj_t obj_in)
{
    if (&mp_type_int != mp_obj_get_type(obj_in)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Domain ID must be a number"));
		return obj_in;
    }

    int  id = mp_obj_get_int(obj_in);
	rmp_domain_id = id;

    return obj_in;
}

/**
 * 
 * 
*/
mp_obj_t setNamespace(mp_obj_t obj_in)
{
    if (&mp_type_str != mp_obj_get_type(obj_in)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Namespace must be a str"));
		return obj_in;
    }

    const char* cstr = mp_obj_str_get_str(obj_in);
    if ((cstr == NULL) || strlen(cstr)==0) {
		mp_raise_ValueError(MP_ERROR_TEXT("Namespace name can not be an null / empty string"));
		return obj_in;
    }

	strncpy(rmp_namespace, cstr, 63);
	return obj_in;
}

/**
 * 
 * 
*/
mp_obj_t setNodeName(mp_obj_t obj_in)
{
    if (&mp_type_str != mp_obj_get_type(obj_in)) {
		mp_raise_TypeError(MP_ERROR_TEXT("Node name must be a str"));
		return obj_in;
    }

    const char* cstr = mp_obj_str_get_str(obj_in);
    if ((cstr == NULL) || strlen(cstr)==0) {
		mp_raise_ValueError(MP_ERROR_TEXT("Node name can not be an null / empty string"));
		return obj_in;
    }

	strncpy(rmp_node_name, cstr, 63);

	return obj_in;
}

void main_timer_callback(rcl_timer_t * timer, int64_t last_call_time)
{
	printf("main Timer:\n");
}

/**
 * 
 * INitialize the ROS Stack creating the base objects needed
 */
mp_obj_t init_ROS_Stack()
{
    printf("\r\nInitializing ROS Stack\r\n");

    init_ROS_Subscriptions();
	init_ROS_Publishers();
    init_mpy_ROS_TypeSupport();

	rmp_rcl_allocator = rcl_get_default_allocator();

	init_options= rcl_get_zero_initialized_init_options();
	RCCHECK(rcl_init_options_init(&init_options, rmp_rcl_allocator));

#ifdef CONFIG_MICRO_ROS_ESP_XRCE_DDS_MIDDLEWARE
	rmw_options = rcl_init_options_get_rmw_init_options(&init_options);

	// Static Agent IP and port can be used instead of auto disvery.
	RCCHECK(rmw_uros_options_set_udp_address((const char*)ROS_AgentIP, (const char *)ROS_AgentPort, rmw_options));
	//## RCCHECK(rmw_uros_discover_agent(rmw_options));
#endif

	// create init_options
	RCCHECK(rclc_support_init_with_options(&rmp_rclc_support, 0, NULL, &init_options, &rmp_rcl_allocator));
	
	// create node
	RCCHECK(rclc_node_init_default(&rmp_rcl_node, rmp_node_name, rmp_namespace, &rmp_rclc_support));
	
	// create executor
	RCCHECK(rclc_executor_init(&rmp_rclc_executor, &rmp_rclc_support.context, 20, &rmp_rcl_allocator));
	uint64_t timeout = 500*1000*1000;
	RCCHECK(rclc_executor_set_timeout(&rmp_rclc_executor, timeout ));

 // create timer,
  	// printf("Main Timer Init\r\n");
  	// const unsigned int timer_timeout = 1000;
  	// int rc = rclc_timer_init_default(&main_timer, &rmp_rclc_support, RCL_MS_TO_NS(timer_timeout), main_timer_callback);
  	// if (rc != RCL_RET_OK)
  	// {
   	// 	printf("Failed to init Timer\r\n");
  	// }
  	// RCCHECK(rclc_executor_add_timer(&rmp_rclc_executor, &main_timer));

	return mp_const_none;
}




/**
 * This is a wrapper function that runs the ROS Stack in a separate MP thread
 * 
 */
  
mp_obj_t mp_run_ROS_Stack()
{
    start_new_ROS_thread(run_ROS_Stack);
    return mp_const_none;
}


/**
 * 
 * 
 * 
*/
void run_ROS_Stack() {

	printf("\r\nROS Task running task\r\n");
	while(1) {
		RCSOFTCHECK(rclc_executor_spin(&rmp_rclc_executor ));

		printf("MicroRos Spinning\r\n");
		const TickType_t xDelay = 2000 / portTICK_PERIOD_MS;
		vTaskDelay( xDelay );
	
	}

}


/**
 * Register a data type which will build a data type instruction set
 * used to marshal data between MicrpROS and Micropython
*/
mp_obj_t registerDataType(mp_obj_t dataMap) {

	mp_obj_t typeName = parseDataTypeDefinition(dataMap, true);

	if  (typeName == NULL) {
		mp_raise_ValueError(MP_ERROR_TEXT("Error registering data type"));
		return mp_const_none;
	}

	return typeName;
}

/**
 * 
 * Diagnostic: Output the instruction list for a registered data type
 * 
*/
mp_obj_t dumpDataType(mp_obj_t dataTypeName) {

	dumpDataTypeMap(dataTypeName);
	return mp_const_none;
}