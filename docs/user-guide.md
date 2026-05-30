# User Guide

ROSMicroPy lets a MicroPython program participate in a ROS 2 graph through micro-ROS. Your program runs on the device, creates publishers and subscriptions, and exchanges normal ROS messages with other ROS nodes through a micro-ROS agent/bridge.

## Mental Model

There are three pieces in a typical setup:

- A ROSMicroPy device running MicroPython and the native ROSMicroPy module.
- A micro-ROS agent reachable over the network.
- A ROS 2 environment that sees the device as a ROS node.

On the device you write Python. Under the hood, ROSMicroPy calls native C functions that create an rclc node, publishers, subscriptions, and type support callbacks.

## Programming Choices

ROSMicroPy supports two styles.

Use the rclpy-style API when you want examples that look like normal ROS 2 Python:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("minimal_publisher")
        self.publisher_ = self.create_publisher(String, "topic", 10)

rclpy.init(bridge_address="192.16.0.50", node_name="minimal_publisher")
node = MinimalPublisher()
rclpy.spin(node)
```

Use the lower-level ROSMicroPy SDK when you want direct access to the native API:

```python
from ROSMicroPy import (
    setNodeName, setAgentIP, setAgentPort,
    init_ROS_Stack, run_ROS_Stack,
    registerDataType, registerROSPublisher, publishMsg,
)
from rostype.Twist import Twist

setNodeName("Turtle1")
setAgentIP("192.16.0.50")
setAgentPort("8888")

init_ROS_Stack()
type_twist = registerDataType(Twist.dataMap)
pub = registerROSPublisher("/turtle1/cmd_vel", type_twist)
run_ROS_Stack()
```

## Message Objects

Generated message classes live under packages such as `std_msgs.msg` and `geometry_msgs.msg`. They inherit from a dictionary-backed `Message` type, so both attribute-style and dictionary-style field access are natural:

```python
from std_msgs.msg import String

msg = String()
msg.data = "hello"
msg["data"] = "hello again"
```

For nested messages, fields are dictionaries:

```python
msg = {
    "linear": {"x": 1.0, "y": 0.0, "z": 0.0},
    "angular": {"x": 0.0, "y": 0.0, "z": 0.5},
}
```

## Current Limits To Keep In Mind

- Type support is allocated into a fixed number of runtime slots.
- Publisher and subscription slots are also fixed-size tables.
- Nested ROS types are supported as fields, but arrays/sequences of nested ROS types are not supported yet.
- The rclpy API is intentionally small. Unsupported calls currently fall through to an `unimplemented` placeholder.
