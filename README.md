# ROSMicroPy

ROSMicroPy brings MicroPython and micro-ROS together so an ESP32-class device can act as a ROS 2 node while still being programmed mostly in Python.

The project has two documentation paths:

- **Use ROSMicroPy**: write MicroPython or rclpy-style programs, configure the bridge/agent, publish messages, subscribe to topics, and use generated message classes.
- **Understand ROSMicroPy**: learn how the MicroPython API is bound into native code, how rclc and micro-ROS are initialized, and how runtime ROS type support serializes Python objects into Micro CDR.

## Documentation

Start here:

- [Documentation index](docs/README.md)
- [End user overview](docs/user-guide.md)
- [rclpy-style programming](docs/rclpy-guide.md)
- [ROSMicroPy MicroPython SDK programming](docs/micropython-sdk-guide.md)
- [Startup and bridge configuration](docs/configuration-and-startup.md)
- [Technical architecture](docs/technical-architecture.md)
- [Type support and serialization internals](docs/type-support-and-serialization.md)

## Examples

The main example directories are:

- `python_example_code/rclpy/`: rclpy-style publisher/subscriber examples.
- `python_example_code/other/`: lower-level ROSMicroPy SDK examples.
- `python_example_code/RMPCore/`: robot-oriented examples.

## Historical Docs

Older documentation has been preserved in `old_docs/`. The current docs in `docs/` are intended to be the maintained entry point.
