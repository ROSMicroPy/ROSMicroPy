# rclpy-Style Programming

The `components/libROSMicroPy/py/rclpy` package provides a small compatibility layer for writing MicroPython programs that resemble standard ROS 2 `rclpy` examples.

It is not a full desktop `rclpy` implementation. It maps the common node, publisher, subscriber, logger, timer, init, and spin calls onto ROSMicroPy native functions.

## Default Example Configuration

The example startup configuration is in `python_example_code/rclpy/config.py`:

```python
BRIDGE_ADDRESS = "192.16.0.50"
AGENT_PORT = "8888"
NAMESPACE = ""
DOMAIN_ID = 0
```

The example helper calls:

```python
rclpy.init(
    bridge_address=BRIDGE_ADDRESS,
    agent_port=AGENT_PORT,
    node_name=node_name,
    namespace=NAMESPACE,
    domain_id=DOMAIN_ID,
)
```

## Publisher Example

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from config import init_rclpy

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("minimal_publisher")
        self.publisher_ = self.create_publisher(String, "topic", 10)

    def publish_once(self):
        msg = String()
        msg.data = "Hello World"
        self.publisher_.publish(msg)

def main(args=None):
    init_rclpy(rclpy, "minimal_publisher", args=args)
    node = MinimalPublisher()
    rclpy.spin(node)
```

## Subscriber Example

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from config import init_rclpy

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__("minimal_subscriber")
        self.subscription = self.create_subscription(
            String,
            "topic",
            self.listener_callback,
            10,
        )

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    init_rclpy(rclpy, "minimal_subscriber", args=args)
    node = MinimalSubscriber()
    rclpy.spin(node)
```

## How rclpy Maps To ROSMicroPy

- `rclpy.init(...)` applies bridge/node configuration and calls `ROSMicroPy.init_ROS_Stack()`.
- `Node(name)` calls `ROSMicroPy.setNodeName(name)`.
- `create_publisher(MsgType, topic, qos)` registers the message type and calls `ROSMicroPy.registerROSPublisher(...)`.
- `publisher.publish(msg)` calls `ROSMicroPy.publishMsg(topic, msg)`.
- `create_subscription(MsgType, topic, callback, qos)` registers the message type and calls `ROSMicroPy.registerEventSubscription(...)`.
- `rclpy.spin(node)` calls `ROSMicroPy.run_ROS_Stack()`.

Message classes provide `get_data_map()`/`dataMap`, which the rclpy shim passes into `registerDataType()` automatically.
