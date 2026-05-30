# Python class: (ROSMicroPy)

## Methods:
 
### ```setDomainID(id:int)```
Sets the domain ID of the ROS Node.
 + Must be called prior to Init

### ```setNamespace(namespace:str)```
Sets the Namespace of the ROS Node.
 + Must be called prior to Init

### ```setNodeName(name:str)```
Sets the NodeName of the ROS Node.
 + Must be called prior to Init

### ```setWifiConfig(sta_id:str, pass:str)```
Configures the ROSNode to attach to a specific SSID (sta_id) with a password. 
 + Must be called prior to Init

### ```registerDataType(mp_obj_t dataMap:rosTypeDataMap)```
Using the dataMap defined by the ROS .msg compiler, create a virtual named type that will be used when receiving or publishing messages. 
 + Init must be called prior

### ```registerEventSubscription(eventName:str, dataTypeName:str, eventCallback)```
Register a callback function that will be called when a named event arrives (i.e. /cmd_vel) This call will marshal the binary data passed in to the event, builds the Micropython representation of that variable and passes that to the registered callback function.
 + Init must be called prior
 + Data type needs to be registered prior

### ```publishMsg(msgPath:str, dataTypeName:str, data:any)```
Publish a ROS Message to the end point defined by msgPath, using a registered data type dataTypeName, along with the Micropython representation of that dataType. ROSMicroPy will populate the data message using named variables, i.e. Geometry_Twist defines two Vector3's named linear and angular. ROSMicroPy will identity those variables by name and will ignore any named variables not defined in the data type.

### ```init_ROS_Stack()```
Initialize the ROS Stack, initializing up the basic ROS infrastructure variables.

### ```run_ROS_Stack()```
Create a Micropython thread and start the execution of the ROS Stack. This call will return right away after establishing the thread. As the thread is created, the GIL ( Micropython's Global interpreter lock ) will be acquired to do some housekeeping, then released while the ROS Thread is spinning. When an event occurs that requires a callback into the interpreter, the GIL will be reacquired then release once the operation in Micropython is complete. This allows for minimal GIL arbitration and smoother Micropython execution
 + Init must be called prior
