# Service Server Mode

Service server mode adds an rclpy-style request/response pattern to ROSMicroPy. A server is created with `Node.create_service()`, and a client uses `Node.create_client()` with either `call_async()` or `call()`.

## Transport Model

The current implementation is topic-backed. For a service named `add_two_ints`, ROSMicroPy creates:

| Direction | Topic | Message type |
| --- | --- | --- |
| Client to server | `add_two_ints/_request` | `AddTwoInts.Request` |
| Server to client | `add_two_ints/_response` | `AddTwoInts.Response` |

This is not a native ROS 2 service entity. It will not appear in `ros2 service list`, and a desktop `rclpy` client or `ros2 service call` cannot call it directly. A non-ROSMicroPy peer can interoperate by publishing and subscribing to the two topics with the matching request and response message types.

## Configure The Agent

Edit `examples/rclpy_services/config.py` before copying the example files to a device:

```python
BRIDGE_ADDRESS = "192.168.8.100"
AGENT_PORT = "8888"
NAMESPACE = ""
DOMAIN_ID = 0
```

The address must point to the host running the micro-ROS agent.

## Server

```python
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.service = self.create_service(
            AddTwoInts,
            "add_two_ints",
            self.handle_request,
        )

    def handle_request(self, request, response):
        response.sum = request.a + request.b
        return response


rclpy.init(
    bridge_address="192.168.8.100",
    node_name="add_two_ints_server",
)
node = AddTwoIntsServer()
rclpy.spin(node)
```

The callback receives a populated request and a new response object. It may mutate and return that response, return a replacement response, or return `None` after mutating the supplied object.

## Asynchronous Client

```python
client = node.create_client(AddTwoInts, "add_two_ints")

request = AddTwoInts.Request()
request.a = 1
request.b = 2

future = client.call_async(request)
future.add_done_callback(lambda done: print(done.result().sum))
```

Keep spinning the node so the response subscription can run. For a blocking request, use `client.call(request)` or:

```python
future = client.call_async(request)
rclpy.spin_until_future_complete(node, future, timeout_sec=5.0)

if future.done():
    print(future.result().sum)
```

## Current Limits

- `wait_for_service()` and `service_is_ready()` currently return `True` without checking graph discovery.
- Requests do not carry a client ID or sequence number. Responses are matched to pending futures in first-in, first-out order.
- Use one client and one server per service name, and avoid overlapping requests when response ownership matters. Multiple clients receive the same response topic and cannot reliably correlate replies.
- Service publishers and subscriptions consume the same fixed runtime slots as normal topic endpoints. One server uses one publisher and one subscription; one active client also uses one of each.
- QoS arguments are accepted for API compatibility but are not currently applied to the native endpoints.

The full runnable pair is in [`examples/rclpy_services/`](../examples/rclpy_services/).
