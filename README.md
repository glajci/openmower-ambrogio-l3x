# Openmower - Ambrogio - L3x
Convert Ambrogio L30 mower to [OpenMower](https://openmower.de) powered mower.

![Demo picture](readme/IMG_7961.JPG?)

> [!WARNING]
> Please be aware that this is a working prototype, any modifications to the mower are made at your own risk.

> [!NOTE]
> Ambrogio L30 mower was used in this project, but it should work with Viper C6, Stiga Autoclip 225 and similar as well.

# Features

* All of the features of the [OpenMower](https://openmower.de)
* Rain sensor
* Lift Sensor
* Emergency Stop push button
* Cutting with 25cm
* Integrated built-in display and top cover buttons (optional)

> Comparison with Yard Force Classic 500
> * Pros:
>   * Increased cutting width (25cm)
>   * More powerful, no issues with cutting the grass
>   * Turns easier due to its geometry
>   * No issues with steep climbs (no wheel spikes needed)
>
> * Cons:
>   * Louder mowing motor (while using 4 points steel cutting blade, perhaps 12 points plastic disc is quieter?)
>   * Tilt sensor not connected

# Hardware and Tools

You will need:

* Ambrogio L30 mower or similar (Viper C6, Stiga Autoclip 225 ...)
* [Open Mower Hardware Kit](https://shop.devops.care/10-openmower)
* [Ardusimple simpleRTK2B – Basic Starter Kit](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/)
* Raspberry Pi 4 (minimum 2GB)
* SD Card 16GB+
* USB Wi-Fi Dongle
* Yard Force Classic 500 wiring harnesses (can be created from the scratch as well)
* 3D printer
* [Vesc Tool Free](https://vesc-project.com/node/17)
* 16x2 LCD Display with I2C adapter (optional)
* Raspberry Pi Zero W + micro Usb Ethernet adapter or Raspberry Pico W (optional)
* 2 relay module (optional)

# Assembly

## Docking station

Remove all the original electronics from the docking station.

![](readme/IMG_7514.JPG?)
![](readme/IMG_7508.JPG?)

Place 2 expansions plugs in 2 holes.

![](readme/IMG_7511.JPG?)
![](readme/IMG_7512.JPG?)

Screw the DC/DC board

![](readme/IMG_7513.JPG?)
![](readme/IMG_7510.JPG?)

> [!NOTE]
> Plug from the YardForce Classic 500 power supply was used here but the original Ambrogio power supply will work as well.
(find the positive and negative wires and connect it appropriately to the DC/DC board)

> [!NOTE]
> For all the voltage and current adjustments please follow the official [OpenMower](https://openmower.de) documentation.


## The mower

Remove all the original mower electronics.
Cut the plastic elements (see the pictures below) to make the place for the mainboard.

![](readme/IMG_7551.JPG?)
![](readme/IMG_7552.JPG?)


### Prepare the motor Hall sensor wires.

![](readme/IMG_7787.JPG?)
![](readme/IMG_7790.JPG?)
![](readme/IMG_7791.JPG?)

### Prepare the motor power wires.

![](readme/IMG_7542.JPG?)

### Ambrogio L30 Opemnower wiring diagram.

![](readme/ambrogio_l30_openmower_wiring_diagram.jpg?)

> [!NOTE]
> YardForce Classic 500 wiring harness was used, since it fits to the OpenMower mainboard sockets, but it can be created from the scratch as well.

> [!NOTE]
> Crimped terminals for the motor power wires were used.

> [!NOTE]
> All 3 motor harnesses have the same colouring.

### Install the main switch into the mower body (power switch from the YardeForce Classic 500 was used here)
> [!NOTE]
> No need to install the power button if 2 relay module and top cover power buttons are integrated (see later in this tutorial).

![](readme/IMG_7516.JPG?)

Remove Ambrogio's power supply socket

![](readme/IMG_7515.JPG?)

Extend the circular hole to give it a rectangular shape with proper dimensions

![](readme/IMG_7517.JPG?)
![](readme/IMG_7518.JPG?)
![](readme/IMG_7519.JPG?)

Insert the power switch

![](readme/IMG_7520.JPG?)

### Prepare the power supply harness.
> [!NOTE]
> Since the Ambrogio batteries have just 2 wires (positive and negative), Shottky diode was used to create separate charge + and battery + signals. (Original YardForce Classic 500 battery plug was use here)

![](readme/IMG_8353.JPG?)
![](readme/IMG_8357.JPG?)

Prepare the power connectors

![](readme/IMG_8354.JPG?)

Connect it to the OpenMower mainboard.

![](readme/IMG_8356.JPG?)

Connect OpenMower with power button (2 relay module visible on the pictures is optional - see later in this tutorial).

![](readme/IMG_8359.JPG?)
![](readme/IMG_8360.JPG?)

### Prepare the lift sensor cable.

![](readme/IMG_7797.JPG?)

### Install the mainboard

Unscrew the original left and right battery holders.
Print and screw the mainboard holders.
> [!NOTE]
> You will find all the 3d models in this repository.

![](readme/IMG_7809.JPG?)
![](readme/IMG_7810.JPG?)
![](readme/IMG_7811.JPG?)

### Prepare the top cover panel harness.

![](readme/IMG_7529.JPG?)
![](readme/IMG_7794.JPG?)
![](readme/IMG_7789.JPG?)

### Connect Emergency Stop push button and rain sensor to the mainboard.

![](readme/IMG_7917.JPG?)

### (Optional) Install the GPS antenna in the mower's body

> [!NOTE]
> There is no need to cut the hole in the mower's body for the GPS antena. It can work inside of the mower as well.
> Installing it like in the pictures below, improve the signal quality

Cut the hole in the mower body.

![](readme/IMG_7521.JPG?)
![](readme/IMG_7522.JPG?)
![](readme/IMG_7523.JPG?)
![](readme/IMG_7524.JPG?)

Install the GPS antena in the body and seal it with the silicone.

![](readme/IMG_7535.JPG?)
![](readme/IMG_7922.JPG?)

Install a piece of steel material from the bottom as the antenna shield.

![](readme/IMG_7928.JPG?)


### (Optional) Install the 2 relay module as power switch.

Use exaclty the same 2 relay module as on the picture below.

![](readme/IMG_7907.JPG?)

Solder the wires from the bottom.

![](readme/IMG_7908.JPG?)

Prepare the wires and the plug for on/off buttons.

![](readme/IMG_7918.JPG?)

Print and screw the 2 relay module adapter.

![](readme/IMG_7924.JPG?)
![](readme/IMG_7925.JPG?)

Connect as show below.

![](readme/IMG_7919.JPG?)
![](readme/IMG_7926.JPG?)
![](readme/IMG_7920.JPG?)

### (Optional) Install the display.

#### Variant 1 - Raspberry Pi Zero W based (recommended)
Print the 3d model.

![](readme/IMG_XXXX.JPG?)

Assemble the Raspberry Pi Zero W and LCD display and connect the wires as shown below.

![](readme/IMG_XXXX.JPG?)
![](readme/IMG_XXXX.JPG?)

Install the display in the mower and connect it with the top cover panel.

![](readme/IMG_XXXX.JPG?)
![](readme/IMG_XXXX.JPG?)
![](readme/IMG_XXXX.JPG?)

Connect the display with Raspberry Pi using Usb - micro Usb cable
Connect the display with Raspberry Pi using Ethernet cable - (micro Usb to Ethernet adapter on Pi Zero side)

![](readme/IMG_XXXX.JPG?)
![](readme/IMG_XXXX.JPG?)

#### Variant 2 - Rasberry Pico W based
Print the 3d model.

![](readme/IMG_7888.JPG?)

Assemble the Raspberry Pico W and LCD display and connect the wires as shown below.

![](readme/IMG_7910.JPG?)
![](readme/IMG_7911.JPG?)

Install the display in the mower and connect it with the top cover panel.

![](readme/IMG_7909.JPG?)
![](readme/IMG_7913.JPG?)
![](readme/IMG_7916.JPG?)

Connect the display with Raspberry Pi using Usb - micro Usb cable

![](readme/IMG_7928.JPG?)
![](readme/IMG_7929.JPG?)


## Software

### Install the OpenMower on the Raspberry Pi

Please follow the official [OpenMower](https://openmower.de) documentation for more details.

### Upload configuration files to xESC

Connect to the xESC which is going to be the mowing motor controller using USB to microUSB cable.

Open Vesc Tool [Vesc Tool Free](https://vesc-project.com/node/17).

Load the following configuration file and write it to the mowing motor xESC.

[Ambrogio_L30_Mower_Motor_10A.xml](configuration/Ambrogio_L30_Mower_Motor_10A.xml)

Connect to the xESC's which are going to be the drive motors controllers using USB to microUSB cable.

Open Vesc Tool [Vesc Tool Free](https://vesc-project.com/node/17).

Load the following configuration file and write it to the drive motor xESC.

[Ambrogio_L30_Drive_Motor.xml](configuration/Ambrogio_L30_Drive_Motor.xml)

> [!NOTE]
> The xESC configuration files provided above are suited for Ambrogio L30 motor. Play with Vesc Tool to find best settings for another motors.

> [!NOTE]
> Please follow the official [Vesc](https://vesc-project.com/documentation) documentation for more details.


### Modify the mower_config.txt

> [!NOTE]
> Please follow the official [OpenMower](https://openmower.de) documentation for more details.

Define the wheel distance and wheel ticks

Set distance between wheels in m
```
export OM_WHEEL_DISTANCE_M=${WHEEL_DISTANCE_M:-0.355}
```
Set default ticks/m
```
export OM_WHEEL_TICKS_PER_M=${OM_WHEEL_TICKS_PER_M:-1830.0}
```
Define the GPS antena offsets, according to the antena position (depends on where the GPS antena is located in the mower)

Set default GPS antenna offset (Example)
```
export OM_ANTENNA_OFFSET_X=${OM_ANTENNA_OFFSET_X:-0.08}
export OM_ANTENNA_OFFSET_Y=${OM_ANTENNA_OFFSET_Y:-0.0}
```

Set the following configuration of the emergency inputs
```
export OM_EMERGENCY_INPUT_CONFIG="L, I, I, !S"
export OM_EMERGENCY_LIFT_PERIOD="100"
export OM_EMERGENCY_TILT_PERIOD="2500"
```

### The display - Variant 1 - Raspberry Pi Zero W + micro Usb to Ethernet adapter (recommended)

Display connects to the OpenMower's MQTT over Ethernet, to both, read and send MQTT messages.

> [!NOTE]
> You will find similar project in [openmower-display](https://github.com/glajci/openmower-display/blob/main/README.md) repository.

#### Features

* Show actual OpenMower state, sensors values (GPS accuracy, Battery voltage, Charging)
* Start, Pause, Dock, Reset Emergency, Skip area, Skip path actions
* Sleep timer turns off display after 60s, wakes on any button press

#### Tools

You will need:

* A [Raspberry Pi Zero W](https://www.raspberrypi.com/news/raspberry-pi-pico-w-your-6-iot-platform/).
* A micro SD Card (at least 8GB)
* A micro USB to Ethernet adapter.
* A 16x2 lcd i2c display.
* A micro-USB cable and Ethernet cable.
* A source code files (included in this repository)
* A computer (presumably, the one you are reading this on!)

Additionally, if your Zero W does not have any GPIO headers pre-attached, you will need:

* A pair of Zero GPIO header pins.
* A soldering iron + solder.
* A breadboard to align the pins while soldering.

##### Setup

Flash Raspberry Pi OS Lite (no desktop) to the SD Card using [RPi Imager](https://www.raspberrypi.com/software)
> [!NOTE]
> Do not forget to configure: hostname, login, password, wifi SSID, wifi password and enable SSH to get access to Pi Zero W later on.

Insert micro SD card to Pi Zero W and power it on. Wait until it starts.

> [!NOTE]
> All examples below are for Windows OS and for user omdisplay and password omdisplay. Please change it accordingly to your setup.

Edit [config.py](pico_zero_w/display/src/config.py) file and set the IP of the Openmower's Rpi Ehternet device.
example
```
mqtt_host = "172.16.78.1"
mqtt_port = 1883
```
> [!NOTE]
> To determine the IP of the Openmower's Rpi Ehternet device, SSH to Openmower Rpi and execute ip addr show eth0

Copy all python (*.py) files from [pico_zero_w/display/src](pico_zero_w/display/src) to Pi Zero W.
example
```
pscp -r -pw omdisplay {your_location}\pico_zero_w\display\src\*.* omdisplay@omdisplay.local:/home/omdisplay
```

SSH to Pi Zero W
example
```
putty -ssh omdisplay.local:22 -l omdisplay -pw omdisplay  
```

Make main.py file executable
```
chmod +x /home/omdisplay/main.py
```

Create new systemd service file
```
sudo nano /etc/systemd/system/omdisplay.service
```

Paste the following content
```
[Unit]
Description=My Python Startup Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/omdisplay/main.py
WorkingDirectory=/home/omdisplay
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

Enable and start the service
```
sudo systemctl daemon-reload
sudo systemctl enable omdisplay.service
sudo systemctl start omdisplay.service
```

The application will now auto-start whenever you supply power to your Pi Zero W.

To check status
```
systemctl status omdisplay.service
```

To see the logs
```
journalctl -u omdisplay.service -f
```


### The display - Variant 2 - Raspberry Pico W

Display connects to the OpenMower's MQTT over WIFI (either via router or directly to OpenMower's Hotspot), to both, read and send MQTT messages.

> [!NOTE]
> You will find similar project in [openmower-display](https://github.com/glajci/openmower-display/blob/main/README.md) repository.

#### Features

* Show actual OpenMower state, sensors values (GPS accuracy, Battery voltage, Charging)
* Start, Pause, Dock, Reset Emergency, Skip area, Skip path actions
* Sleep timer turns off display after 60s, wakes on any button press

#### Tools

You will need:

* A [Raspberry Pi Pico W](https://www.raspberrypi.com/news/raspberry-pi-pico-w-your-6-iot-platform/).
* A 16x2 lcd i2c display.
* A micro-USB cable.
* A UF2 image (included in this repository) for Pico W.
* A computer (presumably, the one you are reading this on!)
* [Thonny](https://thonny.org/).

Additionally, if your Pico W does not have any GPIO headers pre-attached, you will need:

* A pair of Pico GPIO header pins.
* A soldering iron + solder.
* A breadboard to align the pins while soldering.

##### Setup

While holding down the BOOTSEL button on your Pico, connect it to your device via micro-USB cable.

The Pico should present itself as a USB mass storage drive.

Copy the [UF2](display/RPI_PICO_W-20241129-v1.24.1.uf2) file to the root of the drive. Once copied, the storage drive will automatically disconnect, and the Pico is ready for use.

##### Basic Config

There are 2 possible configurations of the display:
1. connecting the display to the same WIFI, the OpenMower is connected
2. connecting the display to the OpenMower's Hotspot (possible if you are using external WIFI USB dongle plugged in the OpenMower's Raspberry Pi with [this](/readme/hotspot.txt.settings) CommitUp configuration of the OpenMower (primary_wifi_device: wlan0)
 * Personally I prefer the option 2, as you will avoid WIFI range issues (Rpi Pico W does not have the external WIFI antenna connector). Connecting the display to the RPi HotSpot will ensure the stable connection. Option 1 will work as well if you have a good WIFI coverage over the mowing areas or if you intend to use it as a Remote Control.
   
Open the following files in the text editor of your choice: `config.py` and `secrets.py`.

In `secrets.py`, you need to provide:

* The SSID and password for your WiFi network or OpenMower Hotspot (prefferable).

Example:
```bash
ssid = "openmower-93"
password = "openmower"
```

In `config.py`, you need to provide:

* The IP address or hostname (openmower.local) of MQTT of the OpenMower, and the MQTT port

Example:
```bash
mqtt_host = "10.41.0.1"
mqtt_port = 1883
```

##### First Run

Once the above steps are complete, connect your Pico W to your machine and open Thonny. Make sure to select the Pico's MicroPython environment on the bottom-right of the Thonny window, then, once connected, upload each of the `.py` files to your device.

**NOTE:** Depending on the UF2 image that you used, you *might* need to install the `urequests` package before running the display for the first time. To do this, uncomment the relavent lines in `mqtt.py`, save to the Pico and then run `main.py` once manually in order for the Pico to connect to your network and install the package. Alternatively, you can install `urequests` to the Pico via Thonny's package manager.

Once installed, stop execution, re-comment or delete the lines, save and re-upload to the Pico.

The application will now auto-start whenever you supply power to your Pico.





After successful installation you should see something like that:

![Main screen](readme/IMG_7932.JPG?)

Turn on the OpenMower, it will try to establish MQTT connection.

![Demo picture](readme/IMG_7977.JPG?)

When the connection is established you should be able to operate the OpenMower:

![Demo picture](readme/IMG_7930.JPG?)

Pressing the Up, Down or Enter button on the top cover panel, you will enter the menu.
Depending on the current mower status you will see one of the submenus.

![](readme/IMG_7935.JPG?)
![](readme/IMG_7987.JPG?)
![](readme/IMG_7988.JPG?)


Using Up and Down arrows on the top cover panel, you can scroll the available submenus.
Pressing Enter will execute the selected menu action (example: Reset Emergency) and return to main view.

When OpenMower operates you will see one of the following statuses.
![](readme/IMG_7936.JPG?)
![](readme/IMG_7937.JPG?)
![](readme/IMG_7939.JPG?)

# Summary

Hopefully, you will manage to follow the instructions and by the end of the day you will enjoy the perfect lawn.

![](readme/IMG_7962.JPG?)
![](readme/IMG_7702.JPG?)
![](readme/IMG_7703.JPG?)
![](readme/IMG_7704.JPG?)

In case of any support request visit the excellent OpenMower community on the dedicated [Discord](https://discord.gg/jE7QNaSxW7) channel.
