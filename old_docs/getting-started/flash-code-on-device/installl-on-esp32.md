
<div style="width:100%">
<table style="background-color:#FEFEF2;width:100%">
<tr style="border:1px solid">
  <td style="width:90%;padding-left:10px;font-size:48pt;color:black;float:left">
    <p style="float:left;">ROSMicroPy</p>
  </td>
  <td>
    <img src="../../images/Logo.png" height="100" style="float:right"></span>
 </td>
 </tr>
 </table>
 </div>
<br/>
<hr/>
<br/>

## Overview
This guide provides step-by-step instructions on how to install ROSMicroPy on an ESP32 device. This procedure is compatible with Linux and macOS. Windows users may need adjustments for WSL2.

## Prerequisites
- **Operating System**: Linux or macOS (procedures may vary for Windows with WSL2).
- **Tools Installed**: Docker, [Thonny Python IDE](https://thonny.org/).

## Supported Devices
- **ESP32 Generic (WROVER)**
- **ESP32-S3 (WROOM1)**

## Installation Steps

### 1. Clone the ROSMicroPy Repository
Begin by cloning the ROSMicroPy repository from GitHub:

```
git clone https://github.com/ROSMicroPy/ROSMicroPy
````

````
* Change directory to the root of the project (ROSMicroPy)
* Run ./startESP32Flash to start the container
````

#### On success you should see the following screen

<img src="./launch_flasher_screenshot.png" width=500></img>

At the command prompt type

**./flash [DEVICE_ID] [erase]**

Replace **[DEVICE_ID]** with one of the following

* **rmp_core_generic**      -> (rmp-core code for a generic ESP32 device)
* **rmp_core_s3**   -> (rmp-core code for an ESP32-S3 device)
* **rmp_cam_generic**    -> (rmp-core + espcam code for and ESP32-S device)
* **rmp_cam_s3** -> (rmp-core + espcam code for an ESP32-S3 'wroom1' device)
* **rmp_core_s6** -> rmp_core for a ESPP32-C6

If parameter #3 = "erase" then the device flash/QSPI flash will be erased to factory reset before programming. 

**WARNING: ALL CONTENT WILL BE LOST with the erase Option**

## On success you should see the following screen

<img src="./FlashTool-Screenshot.png" width=500></img>

## Post Install
* Close the terminal window.
* On the host computer, launch Thonny and verify that the REPL prompt is present. 

<img src="../Thonny_Copy_Wifi.png" width=500/>

## Your device is now ready to be a ROS Node


