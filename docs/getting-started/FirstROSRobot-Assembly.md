<div style="width:100%">
<table style="background-color:#FEFEF2;width:100%">
<tr style="border:1px solid">
  <td style="width:90%;padding-left:10px;font-size:48pt;color:black;float:left">
    <p style="float:left;">ROSMicroPy</p>
  </td>
  <td>
    <img src="../images/Logo.png" height="100" style="float:right"></span>
 </td>
 </tr>
 </table>
 </div>
<br/>
<hr/>
<br/>


**RosMicroPy supports the ESP32 platform**
  * Generic ESP32 (tested on the WROVER-B) 
  * ESP32-S3 (tested on the WROOM-1

## How to initialize a ROSMicroPy board
### Prerequisites:
* Computer with Docker installed
* [Thonny](https://thonny.org/) is Installed
* A clone of this [repo](https://github.com/ROSMicroPy/ROSMicroPy)
* A target ESP32 device 


Change your directory to the top of the ROSMicroPy project.

* Enter the following command **./startFlasher**

If this worked, your CLI prompt should be root@Flasher

* Attach your ESP32 device to the USB/Serial Port

* To run the flasher enter the command **flash [DEVICE]**
Where [DEVICE] can be one of the following;

    * **RMP-Core**        ESP32 Generic device
    * **RMP-Core-S3**     ESP32 S3 Generic device
    * **ESPCAM**          ESP32-S + ESP32Cam
    * **ESPCAM-S3**,      WROOM1 (S3 device + ESP32Cam)
    * **LCD-Controller**  WROOM1 (S3 device + JSONForms/LVGL)

* **You should see bootloader Flashing your device with the ROSMicroPy code**
