# Releases

## rel-july-2026 — July 2026

This release is a substantial update from [`rel-11-16-2024`](https://github.com/ROSMicroPy/ROSMicroPy/releases/tag/rel-11-16-2024), centered on a more Python-native application API, broader type support, updated firmware targets, and easier installation.

### Highlights

- Added the integrated, frozen `rclpy` compatibility layer as the primary application API, including nodes, publishers, subscriptions, timers, logging, spinning, and startup configuration.
- Added topic-backed service server/client mode with service classes, futures, synchronous and asynchronous calls, and `AddTwoInts` examples.
- Reworked dynamic ROS type support and Micro CDR serialization/deserialization, including nested messages, arrays, sequences, strings, generated message classes, and generated service request/response classes.
- Converted the ROSMicroPy integration to the current native MicroPython module/component build and reorganized component dependencies and build wiring.
- Added and refreshed ESP32 camera support, including camera-oriented board/module work.
- Updated ESP32, ESP32-S3, and ESP32-C6 board configuration and release scripts, including ESP32-S3 4 MiB flash and octal-SPIRAM variants.
- Added browser-based firmware installation with ESP Web Tools and published firmware manifests for generic ESP32 and ESP32-S3 Core builds.
- Reorganized examples around the rclpy publisher/subscriber and service workflows; retained direct-ABI examples under `examples/deprecated/`.
- Expanded the user, architecture, startup, rclpy, and type-support documentation and marked the direct `ROSMicroPy` MicroPython ABI as deprecated for new applications.
- Cleaned up bundled components, obsolete assets, old build paths, and submodule configuration.

### Service Mode Notes

Service mode uses `<service>/_request` and `<service>/_response` topics. It does not currently create a native ROS 2 service entity, so native ROS 2 service discovery and `ros2 service call` are not supported. See [Service server mode](readme_docs/server-mode.md) for usage and current concurrency limits.

### Compatibility Notes

- Existing direct-ABI applications can continue to use the `ROSMicroPy` module, but new applications should use `rclpy`.
- Applications should review agent address, port, namespace, and domain settings when moving to the new examples.
- The embedded runtime still uses fixed-size type-support, publisher, and subscription tables.
- Arrays or sequences of nested ROS message types remain unsupported.

See the [complete comparison](https://github.com/ROSMicroPy/ROSMicroPy/compare/rel-11-16-2024...rel-july-2026) for the full change set once the release tag is published.
