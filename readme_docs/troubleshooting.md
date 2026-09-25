# Troubleshooting

## Installer cannot open the device

Use a Web Serial-capable browser and a USB data cable. Close other programs using the serial port and check host serial-device permissions. If necessary, put the board into its bootloader mode according to the board manufacturer's instructions. Select firmware matching the board's chip and memory configuration.

## Device is missing from the ROS graph

1. Confirm Wi-Fi connected before `rclpy.init()` and print `wlan.ifconfig()`.
2. Confirm the agent is running and reachable at the configured LAN address and UDP port 8888.
3. Match the domain ID in the device, agent environment, and desktop ROS tools.
4. Check agent output for an incoming client session.
5. Set node name and namespace during `init()`, then reset the device before retrying.

The embedded `rclpy` default agent IP is `192.16.0.50`; the examples use `192.168.8.100`. Neither is automatically your host address. Set it explicitly.

## Node appears but messages do not arrive

Use `ros2 topic list` and `ros2 topic info /topic` to confirm the resolved topic name and message type. Confirm that the application actually calls `publish()` or creates a timer that publishes. Use `rclpy.spin(node)` to start the native task; `spin_once()` alone does not do so. Keep timer callbacks short.

## Service is absent from `ros2 service list`

This is expected: service mode uses `<name>/_request` and `<name>/_response` topics. Native `ros2 service call` and desktop rclpy service clients cannot call it directly. A future that never completes may indicate an inactive executor, mismatched topic/type, or an absent peer; readiness helpers do not discover peers. See [services](server-mode.md).

## Serialization fails

| Error or symptom | Check |
| --- | --- |
| `missing ROS field` | Supply every field in the registered message definition. |
| `must be a dict` | Use a dictionary for a nested message field. |
| `array requires capicity` | Include the schema's intentionally spelled `capicity` key. |
| `array length mismatch` | Match fixed-array capacity exactly. |
| `exceeds sequence capacity` | Reduce the sequence length or revise its bound. |
| Nested message array fails | Arrays/sequences of nested messages are unsupported. |

For native diagnostics, use `dumpDataType(type_name)` from the [legacy ABI](micropython-sdk-guide.md). Compare field order and capacities with [type support](type-support-and-serialization.md).

## Repeated runs stop working

Native type, publisher, and subscription tables are finite. Python shutdown and node destruction do not release native slots. Reset the device between application runs instead of repeatedly initializing the stack.

When reporting a problem, include the board and firmware revision, agent/ROS distribution, startup configuration without credentials, a minimal program, and device/agent logs.
