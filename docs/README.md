# ROSMicroPy Documentation

ROSMicroPy can be approached from two documentation tracks.

The first track is for end users writing ROS 2-compatible nodes in MicroPython. It covers the rclpy-style compatibility API, the lower-level ROSMicroPy SDK, startup configuration, publishers, subscriptions, and message objects.

The second track is for maintainers and firmware developers. It explains how ROSMicroPy works internally, how MicroPython calls cross into native C, how dynamic type support is registered with micro-ROS, and how message data is marshaled between MicroPython objects, ROSMicroPy C code, Micro CDR, and the micro-ROS transport.

The diagrams use fenced `plantuml` blocks, which are compatible with GitLab Flavored Markdown when PlantUML or Kroki diagram rendering is enabled for the GitLab instance. If diagram rendering is disabled, GitLab still shows the diagram source as a normal code block.

## End User Track

- [User guide](user-guide.md): project model, workflow, and common tasks.
- [rclpy-style programming](rclpy-guide.md): write code using a small subset of the familiar ROS 2 Python API.
- [ROSMicroPy SDK programming](micropython-sdk-guide.md): use the lower-level MicroPython API directly.
- [Startup and bridge configuration](configuration-and-startup.md): configure node name, namespace, ROS domain, bridge IP, and port.

## Technical Track

- [Technical architecture](technical-architecture.md): runtime layers, initialization flow, publishers, subscribers, and threading.
- [Type support and serialization](type-support-and-serialization.md): detailed explanation of type definitions, DXIL instruction lists, type-support slots, serialization, deserialization, sizing, arrays, and sequences.

## Source Material

The previous documentation set is preserved in `old_docs/`. It is useful historical context, but the files in this folder are the current map for the project.
