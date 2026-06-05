# ROSMicroPy

ROSMicroPy brings MicroPython and micro-ROS together so an ESP32-class device can act as a ROS 2 node while still being programmed mostly in Python.

The primary way to write ROSMicroPy applications is the integrated rclpy interface. The goal is practical portability: take a ROS 2 `rclpy` app from your computer and run it on a ROSMicroPy node with minimal changes.

The older direct MicroPython ABI exported through `uros_mp_reg` remains for older code and internal support, but it should be treated as deprecated for new application development.

## Documentation

### End User Track

- [End user overview](readme_docs/user-guide.md)
- [rclpy programming](readme_docs/rclpy-guide.md)
- [Startup and bridge configuration](readme_docs/configuration-and-startup.md)
- [Deprecated MicroPython ABI](readme_docs/micropython-sdk-guide.md)

### Technical Track

- [Technical architecture](readme_docs/technical-architecture.md)
- [Type support and serialization internals](readme_docs/type-support-and-serialization.md)

The diagrams in the documentation use fenced `mermaid` blocks, which GitHub renders directly in Markdown files, issues, pull requests, discussions, and wikis.

## Examples

The main example directories are:

- `python_example_code/rclpy/`: rclpy publisher/subscriber examples.
- `python_example_code/other/`: older direct ABI examples.
- `python_example_code/RMPCore/`: robot-oriented examples.
