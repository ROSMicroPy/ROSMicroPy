# ROSMicroPy


**ROSMicroPy is a tightly coupled integration of MicroROS and Micropython, multithreaded, async message, Python based ROS2 firmware for embedded microprocessor devices** 

## Features Include

### [SDK to control the ROS Stack](../modules/libROSMicroPy/README.md)
+ Start / Stop ROS Stack
+ Set the Address of the ROS Agent
+ Set the Node name of the device
+ Publish messages
+ Subscribe to messages
+ Run a server process
+ Support for all standard ROS and Custom Types
+ On device, dynamic on-the-fly, type creation

### Full Container Support
 How to's on creating the supporting containers include:
 + **[Creating a container for Firmware development](./containerSupport/containerDevEnv.md)**
 + **[Creating a container to run the ROS Agent](./containerSupport/containerROSAgent.md)**
 + **[Creating a container to run TeleopKey from Turtlesim](./containerSupport/containerTeleopKey.md)**
 + **[Creating a container to run graphical ROS apps](./containerSupport/containerROSConsole.md)**

### How to get started 
+ **[Flash device and run](./procudures/flashDevice.md)**
+ **[Introduction to Python / ROS Robot Coder Development](./python-dev/welcome.md)**

+ **[*Advanced:* How to setup the firmware development environment](./procudures/firmwareDeveloperEnvironment.md)**

### Thonny Support
    - **[Plugin to compile ROS Types and store to the device](/docs/thonny/thonnyROSTypeSupportPlugin.md)**

### ROSMicro Type Support

+ **[Running the ROS Type Python generator ](./implementation/typeSupport.md)**

### Compiling ROSMicroPy
 
### Micropython ROS Intergration Details
+ [Build System](./implementation/buildSystem.md)
+ [Connecting the different Threading Models](./implementation/threadingModels.md)
+ [Type Support](./implementation/typeSupport.md)
+ [Subscribing to an event](./implementation/eventSubscription.md)
+ [Callback functions on Message Receive events](./implementation/messageCallback.md)
+ [Publishing ROS messages](./implementation/messagePublishing.md)
+ [ROS Server support](./implementation/rosServer.md)

idf.py -D MICROPY_BOARD=RMP_LCD_CONTROLLER -DMICROPY_BOARD_VARIANT=SPIRAM_OCT -DUSER_C_MODULES=../../../../modules flash