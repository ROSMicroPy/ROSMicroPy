from ROSMicroPy import
  registerDataType, dumpDataType, registerEventSubscription,
 run_ROS_Stack, init_ROS_Stack, registerROSPublisher, publishMsg

from ROSMicroPyCAM import rmp_cam_start
import wifi

print("\r\nInit ROS Stack\r\n")
init_ROS_Stack()
run_ROS_Stack()  

rmp_cam_start()