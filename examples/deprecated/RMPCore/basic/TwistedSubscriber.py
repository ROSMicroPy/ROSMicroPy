
import gc
import time

from ROSMicroPy import registerDataType, dumpDataType,registerEventSubscription,
from ROSMicroPy import run_ROS_Stack, init_ROS_Stack
from ROSMicroPy import setNodeName, setAgentIP, setAgentPort
from rostype.Twist import Twist

def ros_event_callback(data):
    print("Ros did something")
    print(data)

#setNamespace("")
setNodeName("Turtle1")

print("\r\nInit ROS Stack\r\n")
init_ROS_Stack()

print("Registgering Data Type\r\n")
typeName = registerDataType(Twist.dataMap)

print("Registgering Event Subscription\r\n")
registerEventSubscription("/turtle1/cmd_vel", typeName, ros_event_callback)

print("Run ROS Stack\r\n")
run_ROS_Stack()  

    
    
    
    
    