import gc
import time
from ROSMicroPy import registerDataType, dumpDataType, registerEventSubscription, run_ROS_Stack, init_ROS_Stack, setNodeName, setNamespace, setAgentIP, setAgentPort
from ROSMicroPyCAM import  rmp_cam_init, rmp_cam_start_publisher
import wifi

#setNamespace("")
setNodeName("Turtle1")
setAgentIP("192.168.8.100")
setAgentPort("8888")


print("\r\nInit ROS Stack\r\n")
init_ROS_Stack()

rmp_cam_init()

print("Run ROS Stack\r\n")
run_ROS_Stack()

rmp_cam_start_publisher()
