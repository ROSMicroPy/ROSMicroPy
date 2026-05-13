# Native `.mpy` Evaluation

`natmod` contains three components:

- `libROSMicroPy`: the ROS/MicroPython binding code. It is currently structured
  as a MicroPython User C Module for firmware builds. It uses
  `MP_REGISTER_MODULE`, `py/runtime.h`, ESP-IDF, FreeRTOS, and micro-ROS APIs.
  Dynamic native `.mpy` modules need a `py/dynruntime.h` `mpy_init` entry point,
  so this component needs a port before the full ROS API can run as a `.mpy`.
- `micropython-helpers`: MicroPython object helper routines. The implementation
  is C++ and uses `std::stringstream`, which is not a good fit for dynamic
  native `.mpy` linking. Rewriting this helper layer in C avoids libstdc++
  dependencies in the `.mpy`.
- `micro_ros_espidf_component`: the ESP-IDF/micro-ROS dependency. This is now
  kept as a submodule at `natmod/micro_ros_espidf_component`.

The CMake build in this directory produces a native `ROSMicroPy.mpy` adapter
that exposes a `component_report()` function and the existing public API names
as stubs. The stubs raise `NotImplementedError` to make it clear that the
current full ROS implementation is still static-firmware-only.

Build for ESP32-S3:

```sh
./natmod/build_native_mpy.sh
```

The default target is `esp32s3`. The MicroPython native architecture remains
`xtensawin`, and the build uses `xtensa-esp32s3-elf-gcc` when available.
The full implementation build requires generated micro-ROS assets:

```sh
./natmod/prepare_microros.sh
./natmod/build_native_mpy.sh
```

`prepare_microros.sh` runs `micro_ros_espidf_component/libmicroros.mk`, which
creates `natmod/micro_ros_espidf_component/include` and
`natmod/micro_ros_espidf_component/libmicroros.a`.

To build for another ESP target:

```sh
TARGET=esp32 ./natmod/build_native_mpy.sh
TARGET=esp32s2 ./natmod/build_native_mpy.sh
```

To verify the pipeline on the host, use:

```sh
TARGET=host ./natmod/build_native_mpy.sh
```
