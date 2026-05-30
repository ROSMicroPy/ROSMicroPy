# Technical Architecture

ROSMicroPy is layered so Python application code can use ROS concepts while native code owns the micro-ROS and rclc integration.

## Runtime Layers

```plantuml
@startuml
package "MicroPython Application" {
  [rclpy-style app]
  [ROSMicroPy SDK app]
}

package "Python Compatibility Layer" {
  [rclpy shim]
  [generated message classes]
  [rosmicropy_interfaces.Message]
}

package "Native MicroPython Module" {
  [ROSMicroPy.c exports]
  [uros_base_func.c]
  [uros_mesg_func.c]
  [mp_uros_dataTypeParser.c]
  [mp_uros_type_support.c]
}

package "ROS Runtime" {
  [rclc node]
  [rclc executor]
  [micro-ROS rmw]
  [Micro XRCE-DDS]
}

[rclpy-style app] --> [rclpy shim]
[ROSMicroPy SDK app] --> [ROSMicroPy.c exports]
[rclpy shim] --> [ROSMicroPy.c exports]
[generated message classes] --> [rosmicropy_interfaces.Message]
[ROSMicroPy.c exports] --> [uros_base_func.c]
[ROSMicroPy.c exports] --> [uros_mesg_func.c]
[uros_mesg_func.c] --> [mp_uros_type_support.c]
[mp_uros_dataTypeParser.c] --> [mp_uros_type_support.c]
[uros_base_func.c] --> [rclc node]
[uros_base_func.c] --> [rclc executor]
[rclc executor] --> [micro-ROS rmw]
[micro-ROS rmw] --> [Micro XRCE-DDS]
@enduml
```

## Native API Exports

`components/native/ROSMicroPy.c` exposes the native functions into MicroPython. The important public functions are:

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

```plantuml
@startuml
participant "Python app" as App
participant "rclpy/SDK" as Py
participant "uros_mesg_func.c" as Msg
participant "type support slot" as TS
participant "rcl" as RCL

App -> Py: create_publisher(MsgType, topic)
Py -> Msg: registerDataType(dataMap)
Msg -> TS: compile or reuse type
Py -> Msg: registerROSPublisher(topic, type_name)
Msg -> RCL: rclc_publisher_init_default(...)
App -> Py: publisher.publish(msg)
Py -> Msg: publishMsg(topic, msg)
Msg -> RCL: rcl_publish(pub, msg, NULL)
RCL -> TS: cdr_serialize(slot, msg, cdr)
TS --> RCL: serialized CDR bytes
@enduml
```

## Subscription Flow

```plantuml
@startuml
participant "ROS graph" as ROS
participant "rclc executor" as Exec
participant "type support slot" as TS
participant "uros_mesg_func.c" as Msg
participant "Python callback" as Callback

ROS -> Exec: topic data
Exec -> TS: cdr_deserialize(slot, cdr, response)
TS --> Exec: Python dict message
Exec -> Msg: service_callback(response, context)
Msg -> Callback: callback(message)
@enduml
```

## Slot Tables

The current implementation uses fixed-size tables:

- Type-support slots: 20
- Publisher slots: 10
- Subscription slots: 10

This keeps the embedded runtime simple, but it means applications should register only the types, publishers, and subscriptions they need.
