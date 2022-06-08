# README

## Installing the Operating System using Fedora release 34 (Thirty Four)

1) Install the Raspberry Pi Imager <pre> sudo dnf install rpi-imager</pre>
2) Connect the micro SD card into the reader and run the Raspberry Pi Imager<pre> rpi-imager </pre>
3) Choose "Raspberry Pi OS 32-bit" and select the micro SD card for writing
4) Detach the micro SD card and connect to the micro SD interface of your Raspberry Pi
5) Turn on the Raspberry board and wait until the installation finish
6) Then, turn on the interfaces I2C (oled) and 1-Wire (dht22 sensor)

## Installing the Python packages in Raspberry

1) Go to desktp and download the raspberry labs in Github <pre>
cd Desktop
git clone https://github.com/alcidescosta/raspberrypi.git labs</pre>
2) Install Ada Fruit Packages (needs review) <pre>
  cd ~
  sudo apt-get update
  sudo apt-get install build-essential python-dev python3-pip
  sudo apt-get install python-imaging python-smbus
  sudo python3 -m pip install --upgrade pip setuptools wheel
  sudo pip3 install --upgrade setuptools
  sudo pip3 install RPi.GPIO
  sudo pip3 install adafruit-circuitpython-dht
  sudo pip3 install Adafruit-SSD1306 </pre>
3) Power off the system, eject the SD card and make an identical copy<pre>
  sudo dd if=/dev/sdc of=raspian.img bs=4M status=progress 
  sudo dd if=raspian.img of=/dev/sdc bs=4M status=progress</pre>
4) Eject the new copied card and test it in a Raspberry board
5) Repeat step 3 until have one SD card for each raspberry

**Done!** 