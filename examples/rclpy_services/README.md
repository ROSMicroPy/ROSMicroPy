# rclpy Service Example

This example contains a topic-backed `AddTwoInts` server and client for ROSMicroPy.

1. Set the micro-ROS agent address and ROS domain in `config.py`.
2. Copy `config.py` plus either `service_server.py` or `service_client.py` to the device.
3. Run the server and client on separate ROSMicroPy nodes that can reach the same agent.

The service name `add_two_ints` maps to the topics `add_two_ints/_request` and `add_two_ints/_response`. This compatibility layer is not a native ROS 2 service; see the [service server mode guide](../../readme_docs/server-mode.md) for interoperability and concurrency limits.
