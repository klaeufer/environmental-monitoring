Raspberry pi/phidget setup:
===========================

Equipment:
----------
A. 1 USB hub  
B. sensors  
C. phidget IO board  
D. USB cable from phidget board to USB hub  
E. USB data cable from USB hub to raspberry pi  
F. raspberry pi  
G. SD card with operating system  
H. USB cable power supply (5V 1A maximum) for raspberry pi.  
I. power supply for USB hub (comes with USB hub)  
J. power supply for phidget board.  
K. ethernet cable connecting raspberry pi to the router.  

Setup:
------
1. Connect sensors (B) to IO board (C).  
2. Connect power supply (J) to IO board (C).  
3. Connect power supply (I) to USB hub (A).  
4. Connect IO board (C) to USB hub (A) via usb cable (D).  
5. Connect USB hub (A) to raspberry pi (F) via usb cable (E).  
6. Connect ethernet cable (K) to raspberry pi (F). Ethernet cable is plugged directly into your router.
7. Connect power supply for raspberry pi (H) to raspberry pi (F).  
8. Insert SD card with OS and setup from "Raspberry pi setup" (G) into raspberry pi.  

Raspberry pi setup:
-------------------
1. Connect power to raspberry pi via USB connection (small connector) from 5V 1A power supply.   
2. Connect raspberry pi to router via ethernet cable.  
3. Connect mouse and keyboard to raspberry pi.  
4. Insert SD card into raspberry pi  
5. Connect raspberry pi to monitor or television via HDMI cable.  
6. If SD card already has OS on it, skip to step 11.  
7. Take SD card and format it using gparted on a linux machine to format entire SD card as fat32.  
8. Download NOOBS from http://www.raspberrypi.org/downloads and put on SD card.  
9. Insert the SD card and unplug and replug in the raspberry pi.  
10. Choose to install Raspbian OS.   
11. Once Raspbian boots, install software from "Software" section.  
12. Set up networking from "Networking" section.  

Software:
---------
Note: To download files without a browser, use wget.  
Change the password:  
passwd  
The default password for the pi is “raspberry”.  
sudo apt-get update  
libusb  
1. Go to http://sourceforge.net/projects/libusb/files/libusb-1.0/  
2. Look at the latest version, replace 1.0.9 with the version.  
wget http://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-1.0.9/libusb-1.0.9.tar.bz2  
tar -xvjf libusb-1.0.9.tar.bz2  
cd libusb-1.0.9  
sudo ./configure; sudo make; sudo make install  

libphidget

wget www.phidgets.com/downloads/libraries/libphidget.tar.gz
tar -zxvf libphidget.tar.gz
cd libphidget
sudo ./configure; sudo make; sudo make install

To make sure everything works:
wget www.phidgets.com/downloads/examples/phidget21-c-examples.tar.gz
tar -zxvf phidget21-c-examples.tar.gz 
cd phidget21-c-examples-2.1.8.20130723/
gcc HelloWorld.c -o HelloWorld -lphidget21
sudo ./HelloWorld

While running the program, plug in the device and see if output appears. If no output appears, there is a problem! All the issues I've encountered are due to a lack of power. Make sure each device has it's own wall outlet.

sudo apt-get install python-setuptools
sudo easy_install virtualenv

sudo apt-get install git
sudo apt-get install mercurial
sudo apt-get install curl

Networking (assumes connected via eth0 currently):
--------------------------------------------------

sudo apt-get install ssh
sudo update-rc.d ssh defaults
sudo reboot

ifconfig

write down inet addr, Bcast, and Mask for eth0

netstat -nr

write down Gateway address and Destination address.

sudo nano /etc/network/interfaces

For ethernet connection:

The file should read (replace the values with the values you wrote down previously):



auto lo

iface lo inet loopback

iface eth0 inet static
address 192.168.1.135
netmask 255.255.255.0
network 192.168.1.0
broadcast 192.168.1.255
gateway 192.168.1.1

auto wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf

iface default inet dhcp

Run a “sudo reboot” to varify changes work. “ping google.com” to make sure.

For wireless connection (MUST use rtl8192cu/rtl8188CUS wifi adapter!):

auto lo

iface lo inet loopback
iface eth0 inet dhcp

auto wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf

iface default inet static
address 192.168.1.135
netmask 255.255.255.0
network 192.168.1.0
broadcast 192.168.1.255
gateway 192.168.1.1

Also edit the /etc/wpa_supplicant/wpa_supplicant.conf file (filling in your ssid and password):

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="your_ssid"
        psk="your_password"
}

Run a “sudo reboot” to varify changes work. “ping google.com” to make sure.

Next, we need to forward the SSH port. Go to your router's administrative page and forward the external port 1990 to the internal port 22 (SSH) with ip address that you specified for the raspberry pi.

To test, run:
ssh -l pi -p 1990 <ip_address>

