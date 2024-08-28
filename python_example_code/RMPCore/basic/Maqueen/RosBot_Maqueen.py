
import gc
import time

from ROSMicroPy import registerDataType, dumpDataType,registerEventSubscription,
from ROSMicroPy import run_ROS_Stack, init_ROS_Stack
from ROSMicroPy import setNodeName, setAgentIP, setAgentPort

from rostype.Twist import Twist
from rostype.Attachment import Attachment

setNodeName("Turtle1")

def ros_event_callback(data):
    print("Ros did something")
    print(data)
 
def ros_attachment_callback(data):
    print(f"Attachment: [{data}]")
    print(data)
    
print("\r\nInit ROS Stack\r\n")
init_ROS_Stack()

print("Registgering Data Type\r\n")
typeTwist = registerDataType(Twist.dataMap)
dumpDataType(typeTwist)

typeAttach = registerDataType(Attachment.dataMap)
dumpDataType(typeAttach)

print("Registgering Event Subscription\r\n")
registerEventSubscription("/turtle1/cmd_vel", typeTwist, ros_event_callback)

print("Registgering Event Subscription\r\n")
registerEventSubscription("/turtle1/attachment", typeAttach, ros_attachment_callback)

print("Run ROS Stack\r\n")
run_ROS_Stack()  

#while True:
#    print("In Main Thread")
#    time.sleep(2)
    
    
    
    
    
    