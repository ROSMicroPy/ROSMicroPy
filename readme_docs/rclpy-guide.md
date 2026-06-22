# rclpy Programming

The `components/libROSMicroPy/py/rclpy` package is the primary user-facing API for ROSMicroPy applications. It is frozen into the firmware image with ROSMicroPy, so from an application writer's point of view it is the native way to write ROSMicroPy nodes.

The goal is practical portability: take a ROS 2 `rclpy` app from your computer and run it on a ROSMicroPy node with minimal changes. ROSMicroPy currently implements the common node, publisher, subscriber, logger, timer, service/client, future, init, and spin calls used by small embedded nodes.

## Default Example Configuration

The example startup configuration is in `examples/rclpy_pubsub/config.py` and `examples/rclpy_services/config.py`:

```python
BRIDGE_ADDRESS = "192.168.8.100"
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

## Timers

`Node.create_timer(period_seconds, callback)` schedules callbacks while `rclpy.spin()` or `rclpy.spin_once()` is running. Timers are cooperative: long callbacks delay other timers and Python-side work.

```python
self.timer = self.create_timer(1.0, self.timer_callback)
```

## Service Server Mode

ROSMicroPy provides `Node.create_service()`, `Node.create_client()`, `Future`, and `spin_until_future_complete()` for embedded request/response programs. The API looks like rclpy, but the transport currently uses paired ROS topics rather than native ROS 2 service entities.

See [Service server mode](server-mode.md) for setup, examples, topic names, and current limits. Complete examples are in [`examples/rclpy_services/`](../examples/rclpy_services/).

## Implemented API At A Glance

- Lifecycle: `init`, `shutdown`, `try_shutdown`, `ok`, `create_node`.
- Spinning: `spin`, `spin_once`, `spin_until_future_complete`.
- Node: publishers, subscriptions, timers, services, clients, logger, name, namespace, and `destroy_node`.
- Client/future: `call`, `call_async`, `done`, `result`, `exception`, and done callbacks.
- QoS: `QoSProfile`, `qos_profile_default`, and `qos_profile_sensor_data` are accepted compatibility objects; the native runtime currently creates default publishers and subscriptions.

## Porting Notes

- Keep node, publisher, subscription, and callback structure close to normal ROS 2 `rclpy`.
- Keep message types explicit, for example `create_publisher(String, "topic", 10)`.
- Replace desktop-only APIs with small embedded equivalents when needed.
- Configure the micro-ROS agent address with `rclpy.init(...)` or the shared example helper.
- Treat output such as `unimplemented: <name>` as a compatibility boundary, not a successful operation.
