import gc
import time

from ROSMicroPy import registerDataType, dumpDataType,registerEventSubscription,
from ROSMicroPy import run_ROS_Stack, init_ROS_Stack, registerROSPublisher, publishMsg
from ROSMicroPy import setNodeName, setAgentIP, setAgentPort

from rostype.Twist import Twist

print("\r\nInit ROS Stack\r\n")
init_ROS_Stack()

print("Registgering Data Type\r\n")
typeName = registerDataType(Twist.dataMap)

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
