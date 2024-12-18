#ifndef __RMP_CAM_PUBLISHER_H__
#define __RMP_CAM_PUBLISHER_H__

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "py/runtime.h"
#include "py/mpconfig.h"

#include <rcl/rcl.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>


void publish_cam_image();
void cam_timer_callback(rcl_timer_t *timer, int64_t last_call_time);
mp_obj_t init_image_Publisher();

#endif