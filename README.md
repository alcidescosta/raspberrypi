# README
This file contains instructions on how to

* install the Raspberry Pi 3 (model B) operating system using
Fedora Linux release 34 (Thirty Four)
* setup the Raspberry OS
* install the Python required packages

The steps above are required to run the examples of this repo. When
finished, download the labs at <pre>
git clone https://github.com/alcidescosta/raspberrypi.git labs</pre>

Please, make sure you have a micro SD card before proceeding to the
next sections. A micro SD card is necessary to  install the Raspberry
OS.

## Installing the OS

1) Install the Raspberry Pi Imager <pre> sudo dnf install rpi-imager</pre>
2) Connect the micro SD card into the reader and run the Raspberry Pi Imager<pre> rpi-imager </pre>
3) Choose "Raspberry Pi OS 32-bit" and select the micro SD card for writing (you can use an USB adapter if needed)
4) Detach the micro SD card (with or without the USB adaptor) and connect it to the micro SD interface of your Raspberry Pi
5) Turn on the Raspberry board and wait until the installation finish

**Done!** 

## Setting up the OS

The OLED display used in the labs require the I2C interface. In order
to activate the Raspberry I2C interface, follow the steps below:

1) Click on _Raspberry > Preferences > Raspberry Pi Configuration_
2) Click on the "Interface" tab
3) Turn on the I2C and SSH switches

**Done!**  There is no need to reboot the system.

## Installing Python packages

Labs are written in Python 3 and require some additional packages
to work. To install them, just follow the steps below:

1) Install Ada Fruit Packages (needs review) <pre>
  cd ~
  sudo apt-get update
  sudo apt-get install build-essential python-dev python3-pip
  sudo apt-get install python-imaging python-smbus
  sudo python3 -m pip install --upgrade pip setuptools wheel
  sudo pip3 install --upgrade setuptools
  sudo pip3 install RPi.GPIO
  sudo pip3 install adafruit-circuitpython-dht
  sudo pip3 install Adafruit-SSD1306 </pre>

**Done!** 

## References
* Raspberry Pi Documentation, [Installing the Operating System](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system), accessed on Jun 14, 2022;
