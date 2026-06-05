from ROSMicroPy import registerDataType, dumpDataType, registerEventSubscription, run_ROS_Stack, init_ROS_Stack, registerROSPublisher, publishMsg

from rostype.Twist import Twist

import gc
import time
import wifi

print("\r\nInit ROS Stack\r\n")
init_ROS_Stack()

print("Registgering Data Type\r\n")
typeName = registerDataType(Twist.dataMap)
dumpDataType(typeName)

print("Registgering Event Subscription\r\n")
pub = registerROSPublisher("turtle1/cmd_vel", typeName)

print("Run ROS Stack\r\n")
run_ROS_Stack()  

mesg = {
      "linear":  { "x": -2.0, "y": 0.0,  "z": 0.0 },
      "angular": { "x": 2.0,  "y": 0.0,  "z": -2.0 }}

while True:
    print("publish mesg")
    publishMsg(pub, mesg);
    time.sleep(2)
