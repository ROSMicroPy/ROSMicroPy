# Installation and first node

This walkthrough uses a supported ESP32 Core board, a USB data cable, Wi-Fi, and a host running a micro-ROS agent and ROS 2. The repository's agent helper selects ROS 2 Jazzy.

## 1. Install firmware

Open the [browser firmware installer](install/index.html) in a browser with Web Serial support. Connect the board, choose **Install ROSMicroPy Core**, and select its serial port. The manifest provides builds for generic ESP32 and ESP32-S3; verify that the board's flash and memory configuration match the firmware before flashing.

Back up files on the device first: an erase operation removes resident MicroPython programs. Close any serial monitor before opening the installer. If the browser cannot access Web Serial, use the repository's command-line [flash helper](https://github.com/ROSMicroPy/ROSMicroPy/blob/main/flash) from the firmware environment described in [Building firmware](building-firmware.md).

The installer uses the committed binaries from `docs/firmware/`. The documentation workflow does not compile firmware or automatically substitute files from `release/`.

## 2. Start the micro-ROS agent

From a checkout on a Docker-enabled host:

```sh
./startAgent
```

The helper runs `microros/micro-ros-agent:jazzy` and publishes UDP port `8888`. Keep this terminal running. Use the host's LAN address as the device's `bridge_address`; `localhost` on the device refers to the device itself. Allow UDP traffic to port 8888 and use the same ROS domain for the device, agent, and ROS 2 tools. The examples use domain `0`.

## 3. Connect the device to Wi-Fi

Open the MicroPython REPL with a serial editor. Run the following with your network credentials, or save it as `boot.py` on the device:

```python
import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("YOUR_SSID", "YOUR_PASSWORD")
for attempt in range(30):
    if wlan.isconnected():
        break
    time.sleep(1)
if not wlan.isconnected():
    raise RuntimeError("Wi-Fi connection timed out")
print(wlan.ifconfig())
```

Connect Wi-Fi before initializing ROS. The repository's `examples/wifi.py` contains demonstration credentials; replace them before use.

## 4. Run a publisher

Save this as `main.py` on the device, replacing the agent address. `rclpy` and the generated message packages are already frozen into ROSMicroPy firmware.

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloNode(Node):
    def __init__(self):
        super().__init__("hello_device")
        self.publisher = self.create_publisher(String, "hello", 10)
        self.timer = self.create_timer(1.0, self.publish_hello)

    def publish_hello(self):
        message = String()
        message.data = "Hello from ROSMicroPy"
        self.publisher.publish(message)

rclpy.init(
    bridge_address="192.168.8.100",
    agent_port="8888",
    node_name="hello_device",
    domain_id=0,
)
node = HelloNode()
rclpy.spin(node)
```

Reset the device to run `boot.py` and `main.py`. Use one ROS initialization and one native node per device session; reset before restarting an application that has already initialized ROS.

## 5. Verify from ROS 2

In a terminal with your ROS 2 environment sourced:

```sh
export ROS_DOMAIN_ID=0
ros2 node list
ros2 topic list
ros2 topic echo /hello std_msgs/msg/String
```

Expect `/hello_device` in the node list and a message containing `Hello from ROSMicroPy` about once per second. If it does not appear, follow [Troubleshooting](troubleshooting.md).

## Next steps

The [publisher and subscriber examples](https://github.com/ROSMicroPy/ROSMicroPy/tree/main/examples/rclpy_pubsub) share a `config.py`. Copy it beside the selected example and edit the address, port, namespace, and domain before running. See [rclpy programming](rclpy-guide.md) and [services](server-mode.md) for application patterns.
