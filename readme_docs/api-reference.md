# API and compatibility

The implementation lives in [`components/libROSMicroPy/py/rclpy/__init__.py`](https://github.com/ROSMicroPy/ROSMicroPy/blob/main/components/libROSMicroPy/py/rclpy/__init__.py). This is an embedded compatibility API, not a complete desktop `rclpy` distribution.

## Lifecycle and execution

| API | Current behavior |
| --- | --- |
| `init(..., bridge_address=..., agent_port=..., node_name=..., namespace=..., domain_id=...)` | Applies configuration and initializes the native ROS stack. Set the node identity here before creating a `Node`. |
| `configure(...)`, `get_config()` | Update or inspect Python startup settings. Configure before `init()`; changing these settings does not recreate the native node. |
| `create_node(name, namespace="")`, `Node(name, namespace="")` | Create a Python node wrapper. Native state is global, not a separate native node per wrapper. |
| `spin(node)` | Starts the native ROS task once, then runs cooperative Python timers until shutdown or interruption. |
| `spin_once(node)` | Runs ready Python timers and sleeps about 10 ms. Does not start the native executor; timeout arguments are not implemented. |
| `spin_until_future_complete(node, future, timeout_sec=None)` | Calls `spin_once()` until completion or timeout. Requires the native task to have started for network responses. A timeout leaves the future pending. |
| `ok()` | Reports the Python initialization flag. Does not probe agent connectivity. |
| `shutdown()`, `try_shutdown()` | Reset Python lifecycle flags; do not finalize native ROS resources. |
| `node.destroy_node()` | Clears Python endpoint and timer lists; does not free native slots. |

Use one node and one initialization per device session. Reset the device before reinitializing or changing the native node configuration. Do not rely on shutdown or destruction to stop the native task or reclaim endpoint capacity.

## Node operations

| API | Purpose and constraints |
| --- | --- |
| `create_publisher(msg_type, topic, qos_profile=None)` | Registers type support and a native publisher; returns an object with `publish(msg)`. |
| `create_subscription(msg_type, topic, callback, qos_profile=None)` | Registers a native subscription; converts received dictionaries to message objects before the callback. |
| `create_timer(period_seconds, callback)` | Cooperative Python timer, serviced during spinning; supports `cancel()` and `reset()`. |
| `create_service(srv_type, name, callback)` | Request subscription and response publisher; callback receives request and response objects. |
| `create_client(srv_type, name)` | Request publisher; response subscription is created on the first call. |
| `get_logger()` | Console logger supporting `info`, `warning`/`warn`, and `error`. |
| `get_name()`, `get_namespace()` | Return the Python wrapper's stored identity. |

QoS depth integers, `QoSProfile`, `qos_profile_default`, and `qos_profile_sensor_data` are compatibility inputs. Native endpoints use the default rclc publisher/subscription initialization; the supplied policies are not applied.

## Clients and futures

`call_async(request)` returns a `Future`. Inspect it with `done()`, `result()`, and `exception()`, or register `add_done_callback(callback)`. `call(request)` waits without a timeout. Prefer asynchronous requests initiated from a timer while `spin(node)` is active.

`wait_for_service()` and `service_is_ready()` return `True` without discovery. Replies are matched in FIFO order without request identifiers. Use one client and server for each service name and one outstanding request. Read [Service server mode](server-mode.md) before integrating a desktop peer.

## Resource and type limits

| Resource | Current limit |
| --- | --- |
| Dynamic type-support slots | 20 |
| Native publishers | 10 |
| Native subscriptions | 10 |
| Nested dictionary stack | 5 levels |

Services share the endpoint tables. Nested message fields are supported, but arrays and sequences of nested messages are not. See [Type support](type-support-and-serialization.md) for capacities and field encoding.

Unsupported methods may print `unimplemented: <name>` and return `None`. This is not evidence that an operation succeeded. Parameters, actions, general executor/context behavior, and desktop lifecycle/resource management are not implemented by this compatibility layer.
