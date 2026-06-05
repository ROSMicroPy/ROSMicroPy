# User Guide

ROSMicroPy lets a MicroPython program participate in a ROS 2 graph through micro-ROS. Your program runs on the device, creates publishers and subscriptions, and exchanges normal ROS messages with other ROS nodes through a micro-ROS agent/bridge.

## Mental Model

There are three pieces in a typical setup:

- A ROSMicroPy device running MicroPython and the ROSMicroPy runtime module.
- A micro-ROS agent reachable over the network.
- A ROS 2 environment that sees the device as a ROS node.

On the device you write Python with rclpy-style ROS concepts. The rclpy code is frozen into the firmware image with the rest of ROSMicroPy, so it behaves as the project's integrated Python interface.

## Primary Interface

Use the rclpy interface for ROSMicroPy application code. It is the primary interface and is designed so many desktop ROS 2 `rclpy` examples can move onto a ROSMicroPy node with minimal changes:

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

The older direct MicroPython ABI is still present to support rclpy internally and to keep older examples running. Treat it as deprecated for application code.

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
