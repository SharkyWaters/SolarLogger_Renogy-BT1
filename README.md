# Solar Logger for Renogy BT-1 using Cyrils Renogy-BT1 Project

A massive thank you goes to Cyrils for his Renogy-BT1 project available at https://github.com/cyrils/renogy-bt1

The code has been edited to save the output to a log file which is saved in the same directory as the code. The logfile is automatically created and named by prefixing a timestamp of when the logging session was started.

# How to setup the Raspberry Pi on MacOS (program availability on Windows may differ slightly) 

1) Download Raspberry Pi OS from https://www.raspberrypi.com/software/operating-systems/ (I recommend the 32-bit "Raspberry Pi OS (Legacy) with Desktop" option - this should cause the least issues with dependencies)
2) Insert microSD card into computer and flash Raspberry Pi OS image onto it using balenaEtcher. Select the "Flash from file" option and the downloaded image file as the target when prompted. The SD card should appear as "boot" on the Desktop. Eject the microSD card when finished (use Disk Utility "unmount/mount" option to do this if the SD card is not visible on the Desktop). You may need to format the SD card if this does not work. See online for more details regarding the correct formatting option to select.
3) Insert microSD into Raspberry Pi. Plug in microHDMI cable, keyboard, mouse and finally the USB-C power cable. Power on. Wait for Raspberry Pi desktop to appear.
4) Set up the Raspberry Pi by following the prompts on the screen. IMPORTANT FOR LATER - make a note of the username and password. Restart when prompted.
5) Turn on your phone hotspot and connect to it by using the button in the top right of the Raspberry Pi Desktop screen.
6) Click on Raspberry symbol in top left corner. Select "Accessories" and then "Terminal".
7) In the terminal window, click to the right of the "$" sign and type "cd Desktop" (getting the spaces and characters right is very important!) and hit the enter key.
8) Like above, type "git clone https://github.com/SharkyWaters/SolarLogger_Renogy-BT1" and hit the enter button.
9) Like Above, type "pip3 install gatt" and hit the enter button. You should see a successfully installed message.
10) Like Above, type "pip3 install libscrc" and hit the enter button. You should see a successfully installed messag - if you do not, it is likely because you need python3.8. This is easiest to solve by downloading the Raspberry Pi OS version called "Buster".
11) Close the Terminal window using the mouse and clicking the 'x' button in the top right corner.
12) Enable VNC  on the Raspberry Pi. This will allow you to access the Raspberry Pi from your laptop (so you dont need it's own screen/keyboard/mouse). This is following steps from https://learn.sparkfun.com/tutorials/how-to-use-remote-desktop-on-the-raspberry-pi-with-vnc/all . Click on the raspberry icon in the top left desktop corner. Select "Preferences", then "Raspberry Pi Configuration", then select the "Interfaces" tab and click the "enable" option for VNC. Select "OK" and close the window. You should see a VNC icon appear in the top right corner of the desktop. Click on the VNC icon and write down the IP address shown in the top left corner (should be 4 numbers seperated by periods e.g. 192.168.40.10).
13) Download VNC Viewer on your laptop. ENSURE YOUR LAPTOP IS CONNECTED TO THE SAME PHONE HOTSPOT AS THE RASPBERRY PI.  Start the application and enter the IP address from previous step into the search bar at the top and hit the enter button. Click "continue" if a pop-up appears and enter the username and password of your Raspberry Pi. The screen should refresh and you should be able to see the Raspberry Pi desktop.
14)  On the Desktop you should see a file (also commonly called a directory) named SolarLogger_Renogy-BT1. The full name might not be visible. Double click on the file.
15) Double click on the file named "example.py". This should open a new window in an application called Thonny.
16) Using an app such as BLE Scanner, connect to the Renogy BT1 module. The app should give you information about the device. The name should be similar to "BT-TH-EA7D0489". Enter this name in the DEVICE_ALIAS field in line 67 of the code. The BLE app should also give the Advertisement Manufacturer Data which will be very similar to the device name (e.g. <e07dea7d0489>). Enter this in the MAC_ADDR field in line 66 of the code (e.g. as "E0:7D:EA:7D:04:89"). The POLL_INTERVAL can also be changed at this point in line 68 (note that it is 0.1 seconds by default). Click the "Save" button in the top of the Thonny window to save the changes.
17) When the Renogy Charge Controller and BT1 module have been connected and powered up, click the green 'play' button in Thonny to start the logging. You should see red text scrolling in the bottom half of the Thonny window. A file will now automatically be created in the SolarLogger_Renogy-BT1 file starting with "test_" and followed by the date and time in yyyymmddhhmmss format. This file can be copied to a USB when the testing has concluded and opened in Excel for processing. If the bluetooth connection is not establishe, try closing Thonny and/or turning the bluethooth on/off from the top right corner of the Raspberry Pi desktop. Logging can be stopped by pressing the red "Stop" button in Thonny.


# Below README info is from Cyrils/Renogy-BT1

Python library to read Renogy RS232 compatible [BT-1](https://www.renogy.com/bt-1-bluetooth-module-new-version/) bluetooth adapter. Tested with **Rover** / **Wanderer** series charge controllers and **Raspberry Pi Zero 2 W**. It might also work with other  "SRNE like" devices like Rich Solar, PowMr, WEIZE etc.

## Example

```
pyhton3 ./example.py
```
Make sure to update `mac_address` and `alias` in example.py. It has APIs to continuously read data or turn on/off load.

**How to get mac address?**

Use any BLE scanner apps like [BLE Scanner](https://play.google.com/store/apps/details?id=com.macdom.ble.blescanner) and look for devices with alias `BT-TH-XXXX..`

**Output**

```
INFO:root:Adapter status - Powered: True
INFO:root:Starting discovery...
INFO:root:Devices found: 5
INFO:root:Found bt1 device BT-TH-B00FXXXX  [XX:6F:B0:0F:XX:XX]
INFO:root:[80:6f:b0:0f:xx:xx] Discovered, alias = BT-TH-B00FXXXX
INFO:root:[80:6F:B0:0F:XX:XX] Connected
INFO:root:[80:6f:b0:0f:xx:xx] Discovered, alias = BT-TH-B00FXXXX
INFO:root:[80:6f:b0:0f:xx:xx] Discovered, alias = BT-TH-B00FXXXX
INFO:root:[80:6F:B0:0F:XX:XX] Resolved services
INFO:root:subscribed to notification 0000fff1-0000-1000-8000-00805f9b34fb
INFO:root:found write characteristic 0000ffd1-0000-1000-8000-00805f9b34fb
INFO:root:resolved services
DEBUG:root:create_read_request 256 => [255, 3, 1, 0, 0, 30, 209, 224]
INFO:root:characteristic_enable_notifications_succeeded
INFO:root:characteristic_write_value_succeeded
DEBUG:root:{'battery_percentage': 100, 'battery_voltage': 14.4, 'controller_temperature': 37, 'battery_temperature': 25, 'load_voltage': 14.4, 'load_current': 1.3, 'load_power': 1, 'pv_voltage': 19.2, 'pv_current': 5.26, 'pv_power': 101, 'max_charging_power_today': 276, 'max_discharging_power_today': 6, 'charging_amp_hours_today': 59, 'discharging_amp_hours_today': 2, 'power_generation_today': 797, 'power_generation_total': 10960, 'charging_status': 'mppt'}
INFO:root:Gracefully exit: Disconnecting device: BT-TH-B00FXXXX [80:6F:B0:0F:XX:XX]
```


## Dependencies

```
pip3 install gatt
pip3 install libscrc
```

## References

 - [Olen/solar-monitor](https://github.com/Olen/solar-monitor)
 - [corbinbs/solarshed](https://github.com/corbinbs/solarshed)
 - [Rover 20A/40A Charge Controller—MODBUS Protocol](https://docs.google.com/document/d/1OSW3gluYNK8d_gSz4Bk89LMQ4ZrzjQY6/edit)

