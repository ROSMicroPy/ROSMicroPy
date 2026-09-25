# Building firmware

Firmware builds use the checked-in MicroPython submodule, ROSMicroPy native components, board definitions, and ESP-IDF. The current `startDevEnv` helper selects `Dockerfile-IDF55.DevEnvironment`, based on `espressif/idf:release-v5.5`. Its container name includes `5.5.1`, but the Docker base is a release branch rather than an immutable version.

## Prepare the checkout

```sh
git clone --recurse-submodules https://github.com/ROSMicroPy/ROSMicroPy.git
cd ROSMicroPy
git submodule update --init --recursive
./startDevEnv
```

Run the helper from the repository root on a Linux host with Docker. It mounts the checkout at `/opt/rosmicropy`, exposes `/dev`, and uses privileged mode and host networking. It opens a shell inside the build container.

## Compile a board

Inside the container, for example:

```sh
cd /opt/rosmicropy
sh ./build_RMPCore_S3.sh
```

The board scripts clean the MicroPython ESP32 build tree, run `mkdirs.sh` and `components/prepare_microros.sh`, invoke `idf.py`, and copy results to `release/`. Run one board build at a time because they share a build directory. Inspect the selected script before running it: it removes previous build outputs, and the shell scripts do not consistently stop at the first failed command. Check the build log and resulting binaries before distributing them.

## Board targets

A board configuration or build script indicates a development target; it is not a claim that every hardware variant has been tested.

| Target | Build script | Browser installer |
| --- | --- | --- |
| Generic ESP32 Core | `build_RMPCore_Generic.sh` | Included |
| ESP32-S3 Core | `build_RMPCore_S3.sh` | Included |
| ESP32-C3 Core | `build_RMPCore_C3.sh` | Not included |
| ESP32-C5 Core | `build_RMPCore_C5.sh` | Not included |
| ESP32-C6 Core | `build_RMPCore_C6.sh` | Not included |
| Generic ESP32 camera | `build_RMP_CAM_Generic.sh` | Not included |
| ESP32-S3 camera | `build_RMP_CAM_S3.sh` | Not included |

Board settings live under [`boards/esp32/`](https://github.com/ROSMicroPy/ROSMicroPy/tree/main/boards/esp32). Inspect the board's CMake configuration, SDK configuration, partition table, flash size, and PSRAM variant before selecting a build. The LCD controller configuration is also present, without a corresponding top-level build helper.

## Build outputs and flashing

Scripts copy the application `.bin`, bootloader `.bin`, partition table `.bin`, ELF, and map file to `release/`. The top-level `flash` helper expects this directory at `/opt/rosmicropy/release` and an environment providing `esptool.py`.

```sh
# Inside the firmware environment, with the board connected:
./flash rmp_core_s3
```

An optional `erase` argument wipes device storage, including MicroPython application files. Check the selected target's offsets and memory settings in the helper before use. C3 and C5 build scripts exist, but the current flash helper does not provide matching branches for those targets.

## Frozen Python modules and interfaces

`components/libROSMicroPy/manifest.py` freezes `components/libROSMicroPy/py/`. This includes the `rclpy` compatibility package, message classes, service classes, and `rosmicropy_interfaces.py`.

`tools/generate_rosmicropy_interfaces.py` generates Python interfaces from ROS `.msg` and `.srv` sources at the paths listed in its `SOURCES` constant. Prepare those sources before invoking it, review the generated changes, and rebuild firmware to freeze the updated classes. Generation does not remove serializer restrictions such as the lack of nested message arrays.

## Refresh the browser installer

After validating generic ESP32 and ESP32-S3 release binaries:

```sh
sh docs/sync-firmware.sh
python tools/build_docs.py
```

The sync script copies the six Core firmware files into `docs/firmware/`. Review and commit those files together with any necessary `docs/manifest.json` changes. The Pages workflow publishes committed installer assets; it does not build or validate firmware on hardware.
