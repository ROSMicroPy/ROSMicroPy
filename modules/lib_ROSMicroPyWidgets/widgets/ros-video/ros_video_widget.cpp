#include "mp_uros_sdk.h"
#include "ros_video_widget.h"

 

#include <rclc/rclc.h>
#include <rclc/executor.h>

#include <micro_ros_utilities/string_utilities.h>
#include <micro_ros_utilities/type_utilities.h>
#include <rosidl_typesupport_introspection_c/message_introspection.h>

#include "esp_littlefs.h"


void ros_video_service_callback( const void *response, void *context) {
    printf("Image received\r\n");

    const sensor_msgs__msg__CompressedImage *image = (const sensor_msgs__msg__CompressedImage  *) response;
    printf("Image received, size = %d\r\n", image->data.size);

    ros_video_widget *instance  = (ros_video_widget *)context;
    //instance->img_dsc.data = (const u_int8_t *)&image->data.data;
    //instance->img_dsc.data_size = image->data.size;
    //lv_img_set_src(instance->img, &instance->img_dsc);
    //lv_obj_center(instance->img);

    char filename[32];
    static int frameCounter = 0;

    sprintf(filename, "/littlefs/image%d.jpg", frameCounter);
    printf("Writting file %s", filename);
	FILE* fp=fopen(filename,"w");
	if (!fp)
	{
	    printf("Unable to open file!\r\n");
	}
    else
    {
	    fwrite(image->data.data, image->data.size, 1, fp);
	    fclose(fp);
    }
	
    frameCounter++;
    if (frameCounter > 10) frameCounter=1; 


};


ros_video_widget::ros_video_widget() {
};

ros_video_widget::ros_video_widget(mpy_LvObject* parent) {

  // Set the quality of service
//   rclcpp::QoS video_qos(10);
//   video_qos.keep_last(10);
//   video_qos.best_effort();
//   video_qos.durability_volatile();  
//   // Subscribe to image topics
//   auto subscription_ = g_node->create_subscription<sensor_msgs::msg::Image>(
//        "image", video_qos, image_callback);


    int rc;
   
    static micro_ros_utilities_memory_conf_t conf = {};

    // OPTIONALLY this struct can configure the default size of strings, basic sequences and composed sequences

    conf.max_string_capacity = 50;
    conf.max_ros2_type_sequence_capacity = 15000;
    conf.max_basic_type_sequence_capacity = 15000;

    // OPTIONALLY this struct can store rules for specific members
    // !! Using the API with rules will use dynamic memory allocations for handling strings !!

    static micro_ros_utilities_memory_rule_t rules[] = {
        {"header.frame_id", 30},
        {"format", 4},
        {"data", 80000}};
    conf.rules = rules;
    conf.n_rules = sizeof(rules) / sizeof(rules[0]);

    printf("Create Message Memory\r\n");
    micro_ros_utilities_create_message_memory(
      ROSIDL_GET_MSG_TYPE_SUPPORT(sensor_msgs, msg, CompressedImage),
      &img_msg,
      conf);

    printf("RosVideo create sub\r\n");
	RCCHECK(rclc_subscription_init_default(
	    &rcl_subscription,
		&rmp_rcl_node,
        ROSIDL_GET_MSG_TYPE_SUPPORT(sensor_msgs, msg, CompressedImage), 
        topicName)
	);


    printf("RosVideo add sub\r\n");
	RCCHECK(rclc_executor_add_subscription_with_context(
		&rmp_rclc_executor,
		&rcl_subscription,
	    &img_msg,
		&ros_video_service_callback, 
        this,ON_NEW_DATA));

    printf("ROS create img\r\n");
    lvObject = lv_img_create(parent->lvObject);
    lv_obj_set_size(lvObject, lv_pct(100), lv_pct(100));
    lv_obj_clear_flag(lvObject, LV_OBJ_FLAG_SCROLLABLE); 

    //img_dsc.header.always_zero = 0;
    //img_dsc.header.w = LV_IMG_CF_UNKNOWN;
    //img_dsc.header.h = LV_IMG_CF_UNKNOWN;
    //img_dsc.header.cf = LV_IMG_CF_RAW;  

    printf("ROS Video init complete\r\n");
    
    const esp_vfs_littlefs_conf_t lfsconf = {
        .base_path = "/littlefs",
        .partition_label = "vfs",
        .format_if_mount_failed = false,
        .dont_mount = false,
    };

    // Use settings defined above to initialize and mount LittleFS filesystem.
    // Note: esp_vfs_littlefs_register is an all-in-one convenience function.
    esp_err_t ret = esp_vfs_littlefs_register(&lfsconf);

    if (ret != ESP_OK) {
        if (ret == ESP_FAIL) {
            printf("Failed to mount or format filesystem\r\n");
        } else if (ret == ESP_ERR_NOT_FOUND) {
            printf("Failed to find LittleFS partition\r\n");
        } else {
            printf("Failed to initialize LittleFS (%s)", esp_err_to_name(ret));
        }
    }   

    size_t total = 0, used = 0;
    ret = esp_littlefs_info(lfsconf.partition_label, &total, &used);
    if (ret != ESP_OK)
    {
        printf("Failed to get LittleFS partition information (%s)", esp_err_to_name(ret));
    }
    else
    {
        printf("Partition size: total: %d, used: %d", total, used);
    }
};


