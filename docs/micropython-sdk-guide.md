# ROSMicroPy MicroPython SDK Guide

The lower-level SDK is exposed by the native `ROSMicroPy` MicroPython module. It gives direct access to startup, type registration, publisher creation, subscription creation, and message publishing.

## Startup

Set configuration before calling `init_ROS_Stack()`:

```python
from ROSMicroPy import setNodeName, setAgentIP, setAgentPort, init_ROS_Stack

setNodeName("Turtle1")
setAgentIP("192.16.0.50")
setAgentPort("8888")

init_ROS_Stack()
```

Optional configuration includes `setNamespace(...)` and `setDomainID(...)`.

## Register A Type

Types are registered from a Python data map:

```python
from ROSMicroPy import registerDataType, dumpDataType
from rostype.Twist import Twist

type_twist = registerDataType(Twist.dataMap)
dumpDataType(type_twist)
```

`registerDataType()` returns the message type name. That returned string is passed to publisher and subscription registration.

## Publish

```python
from ROSMicroPy import registerROSPublisher, publishMsg, run_ROS_Stack

pub = registerROSPublisher("/turtle1/cmd_vel", type_twist)
run_ROS_Stack()

msg = {
    "linear": {"x": -2.0, "y": 0.0, "z": 0.0},
    "angular": {"x": 2.0, "y": 0.0, "z": -2.0},
}

publishMsg(pub, msg)
```

The message shape must match the registered type definition. Missing fields raise a Python exception during serialization.

## Subscribe

```python
from ROSMicroPy import registerEventSubscription, run_ROS_Stack

def ros_event_callback(data):
    print("received")
    print(data)

registerEventSubscription("/turtle1/cmd_vel", type_twist, ros_event_callback)
run_ROS_Stack()
```

Deserialized messages arrive as dictionary-backed Python objects.

## Useful Diagnostics

`dumpDataType(type_name)` prints the compiled instruction list for a type. This is the first thing to check when a message does not serialize the way you expect.
