# Startup And Bridge Configuration

ROSMicroPy must know how to reach the micro-ROS agent before the ROS stack is initialized.

## rclpy Configuration

ROSMicroPy applications configure startup through `rclpy.init(...)`:

```python
rclpy.init(
    bridge_address="192.16.0.50",
    agent_port="8888",
    node_name="minimal_publisher",
    namespace="",
    domain_id=0,
)
```

`bridge_address` is an alias for `agent_ip`.

The examples centralize this in `python_example_code/rclpy/config.py`.

## Deprecated ABI Configuration

The deprecated MicroPython ABI uses setters:

```python
setNodeName("Turtle1")
setAgentIP("192.16.0.50")
setAgentPort("8888")
setDomainID(0)
```

Call these before `init_ROS_Stack()`. This path is retained for older code and internal support; prefer `rclpy.init(...)` for application code.

## Runtime Defaults

If Python code does not set values, runtime startup applies defaults in `init_ROS_Stack()`:

- Node name: `turtle2`
- Agent IP: `192.168.8.100`
- Agent port: `8888`

The integrated rclpy interface overrides the agent IP with its own default, currently `192.16.0.50`, before calling runtime initialization.

## Startup Sequence

```mermaid
sequenceDiagram
    actor User
    participant App as MicroPython app
    participant Py as rclpy
    participant Runtime as ROSMicroPy runtime module
    participant RCLC as rclc / micro-ROS
    participant Agent as micro-ROS Agent

    User->>App: run program
    App->>Py: set node and bridge config
    Py->>Runtime: setAgentIP/setAgentPort/setNodeName
    App->>Py: init
    Py->>Runtime: init_ROS_Stack()
    Runtime->>Runtime: init publishers/subscriptions/type support
    Runtime->>RCLC: init options and UDP agent address
    RCLC->>Agent: connect through Micro XRCE-DDS
    Runtime->>RCLC: create support, node, executor
    App->>Py: register publishers/subscriptions
    App->>Py: spin
    Py->>Runtime: run_ROS_Stack()
    Runtime->>RCLC: executor spin loop
```
