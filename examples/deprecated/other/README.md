# ROSMicroPy example Python code

## Twisted Example

[TwistedPublisher](./TwistedPublisher.py) and [TwistedSubscriber](./TwistedSubscriber.py)
are parallel examples of the int32 publisher and subscriber included with micro-ROS, except they use a `geometry_msgs/Twist` message to test a more complex type.

# ESP32 Maqueen Battle Bots

This project consists of MicroROS running on an ESP32 and ROS2 Agent running on a Host computer. 

The ESP32-based Turtle bot consists of off-the-shelf parts: the Maqueen Turtle bot from [DFRobot](https://www.dfrobot.com/product-1783.html), two [MBits ESP32](https://www.aliexpress.us/item/3256803353734572.html) boards in the [Micro:bit](https://microbit.org) form factor, and a [joystick controller](https://www.amazon.com/Elecfreaks-microbit-Joystick-Wireless-Control/dp/B08HD557QJ).

***Note: on the Joystick controller, P0 needs to be jumped to P9. P0 is an ADC on ADC Block2 which is not usable when Wifi is enabled. P9 is on ADC1***

This [Micro:bit extension board](https://www.aliexpress.us/item/3256805550646047.html) makes that easier.

# Links
### [MBits Wiki](https://www.elecrow.com/wiki/index.php?title=Mbits)

### [Code for the Turtle Bot](RosBot_Maqueen.py)

### [Code for the Joystick V2](RosBot_Teleop.py)
