# Technical Architecture

ROSMicroPy is layered so Python application code uses the integrated rclpy interface while the C runtime owns the micro-ROS and rclc integration.

## Runtime Layers

```mermaid
flowchart TD
    subgraph App["MicroPython Application"]
        RclpyApp["rclpy app"]
        LegacyApp["deprecated ABI app"]
    end

    subgraph Py["Python Compatibility Layer"]
        Rclpy["frozen rclpy package"]
        MsgClasses["generated message classes"]
        MessageBase["rosmicropy_interfaces.Message"]
    end

    subgraph Runtime["ROSMicroPy C Runtime"]
        Exports["ROSMicroPy.c exports"]
        Base["uros_base_func.c"]
        Msg["uros_mesg_func.c"]
        Parser["mp_uros_dataTypeParser.c"]
        TypeSupport["mp_uros_type_support.c"]
    end

    subgraph ROS["ROS Runtime"]
        Node["rclc node"]
        Executor["rclc executor"]
        RMW["micro-ROS rmw"]
        XRCE["Micro XRCE-DDS"]
    end

    RclpyApp --> Rclpy
    LegacyApp --> Exports
    Rclpy --> Exports
    MsgClasses --> MessageBase
    Exports --> Base
    Exports --> Msg
    Msg --> TypeSupport
    Parser --> TypeSupport
    Base --> Node
    Base --> Executor
    Executor --> RMW
    RMW --> XRCE
```

## Deprecated ABI Exports

`components/libROSMicroPy/mp_uros_modules/uros_mp_reg.c` registers the direct `ROSMicroPy` MicroPython functions. That ABI exists to support the integrated rclpy interface and older code; it should be treated as deprecated for application development:

- `init_ROS_Stack()`
- `run_ROS_Stack()`
- `setDomainID(...)`
- `setNamespace(...)`
- `setNodeName(...)`
- `setAgentIP(...)`
- `setAgentPort(...)`
- `registerDataType(...)`
- `dumpDataType(...)`
- `registerROSPublisher(...)`
- `registerEventSubscription(...)`
- `publishMsg(...)`

## Initialization

`init_ROS_Stack()` performs the native setup:

- Initializes subscription slots.
- Initializes publisher slots.
- Initializes dynamic type-support slots.
- Applies native defaults for node name, agent IP, and port if Python did not configure them.
- Creates `rcl_init_options_t`.
- Sets the micro-ROS UDP agent address.
- Creates rclc support, node, and executor.
- Sets executor timeout.

`run_ROS_Stack()` starts the ROS spin loop. It repeatedly enters the MicroPython GIL, spins the rclc executor, exits the GIL, and delays.

## Publisher Flow

```mermaid
sequenceDiagram
    participant App as Python app
    participant Py as rclpy
    participant Msg as uros_mesg_func.c
    participant TS as type support slot
    participant RCL as rcl

    App->>Py: create_publisher(MsgType, topic)
    Py->>Msg: register message type
    Msg->>TS: compile or reuse type
    Py->>Msg: create publisher
    Msg->>RCL: rclc_publisher_init_default(...)
    App->>Py: publisher.publish(msg)
    Py->>Msg: publish message
    Msg->>RCL: rcl_publish(pub, msg, NULL)
    RCL->>TS: cdr_serialize(slot, msg, cdr)
    TS-->>RCL: serialized CDR bytes
```

## Subscription Flow

```mermaid
sequenceDiagram
    participant ROS as ROS graph
    participant Exec as rclc executor
    participant TS as type support slot
    participant Msg as uros_mesg_func.c
    participant Callback as Python callback

    ROS->>Exec: topic data
    Exec->>TS: cdr_deserialize(slot, cdr, response)
    TS-->>Exec: Python dict message
    Exec->>Msg: service_callback(response, context)
    Msg->>Callback: callback(message)
```

## Slot Tables

The current implementation uses fixed-size tables:

- Type-support slots: 20
- Publisher slots: 10
- Subscription slots: 10

This keeps the embedded runtime simple, but it means applications should register only the types, publishers, and subscriptions they need.
