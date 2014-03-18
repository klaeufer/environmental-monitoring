Raspberry pi/phidget setup:
===========================

Raspberry Pi Tutorial:
======================
1. Raspberry Pi OS Install (Raspbian). Skip this step if already using an SD card with Raspbian on it.
#. Raspberry Pi Software Install. Skip this step if using an SD card with software on it.
#. Raspberry Pi Networking Setup. Cannot skip this step.
#. Final Equipment Setup

Raspberry Pi OS Install (Raspbian):
===================================

Equipment required:
-------------------
A. 1 USB hub
B. USB data cable for USB hub to raspberry pi (comes with USB hub)
C. raspberry pi
D. Raspberry Pi power supply (5V 1A or higher) with USB connection
E. 4GB or greater SD card
F. power supply for USB hub (comes with USB hub)  
G. ethernet cable connecting Raspberry Pi to router.
H. USB mouse
I. USB keyboard
J. HDMI cable (male to male).
K. Monitor or television with HDMI port.
L. Linux computer with SD card reader. Can be done on Windows, but you're on your own.

Instructions:
-------------
1. Insert blank SD card with at least 4GB capacity (E) into computer with SD card reader (L).
#. Take SD card and format it using "gparted" on a linux machine to format entire SD card as fat32. This can also be done on Windows, but you're on your own. 
#. Download NOOBS from http://www.raspberrypi.org/downloads and put on SD card.
#. Connect USB hub (A) using data cable (B) to raspberry pi (C).
#. Insert SD card (E) into Raspberry Pi (C).
#. Connect power supply for USB hub (F) to USB hub (A).
#. Connect mouse and keyboard (H and I) to USB hub (A).
#. Connect monitor or television with HDMI port (K) to Raspberry Pi (C) via HDMI cable (J). Make sure you change your TV's input to HDMI.
#. Connect power supply for Raspberry Pi (D) into Raspberry Pi (C).
#. When the Raspberry Pi boots up, choose to install Raspbian.

Raspberry Pi Software Install:
==============================
.. code-block:: bash

    sudo apt-get update
    sudo apt-get install python-setuptools
    sudo easy_install virtualenv
    sudo easy_install pip

    sudo apt-get install git
    sudo apt-get install mercurial
    sudo apt-get install curl

Raspberry Pi Networking Setup:
==============================
1. Plug Ethernet cable from router into Raspberry Pi directly.
2. Connect USB Hub 

Networking (assumes connected via eth0 currently):
--------------------------------------------------

.. code-block:: bash
    sudo apt-get install ssh
    sudo update-rc.d ssh defaults
    sudo reboot

    ifconfig

write down inet addr, Bcast, and Mask for eth0.

.. code-block:: bash
    netstat -nr

write down Gateway address and Destination address.

.. code-block:: bash
    sudo nano /etc/network/interfaces

Choose if you want to use WiFi or Ethernet.

Ethernet:
---------

The file (/etc/network/interfaces) should read (replace the values with the values you wrote down previously)::

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

Run::
    sudo reboot
    ping google.com

WiFi (MUST use RTL8192CU or RTL8188CUS WiFi Adapter!):
------------------------------------------------------

.. code-block:: bash

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

Also edit the /etc/wpa_supplicant/wpa_supplicant.conf file (filling in your ssid and password)::

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="your_ssid"
        psk="your_password"
    }

Run::
    sudo reboot
    ping google.com

Next, we need to forward the SSH port. Go to your router's administrative page and forward the external port 1990 to the internal port 22 (SSH) with ip address that you specified for the raspberry pi.

To test, run:
ssh -l pi -p 1990 <ip_address>

Phidgets Tutorial:
==================

Phidgets Software Install:
==============================
.. code-block:: bash

    sudo apt-get update

libusb:

1. Go to http://sourceforge.net/projects/libusb/files/libusb-1.0/
2. Look at the latest version, replace 1.0.9 with the version::

    wget http://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-1.0.9/libusb-1.0.9.tar.bz2
    tar -xvjf libusb-1.0.9.tar.bz2
    cd libusb-1.0.9
    sudo ./configure; sudo make; sudo make install

libphidget::

    wget www.phidgets.com/downloads/libraries/libphidget.tar.gz
    tar -zxvf libphidget.tar.gz
    cd libphidget
    sudo ./configure; sudo make; sudo make install

To make sure everything works::

    wget www.phidgets.com/downloads/examples/phidget21-c-examples.tar.gz
    tar -zxvf phidget21-c-examples.tar.gz 
    cd phidget21-c-examples-2.1.8.XXXXXXXXX/
    gcc HelloWorld.c -o HelloWorld -lphidget21
    sudo ./HelloWorld

While running the program, plug in the device and see if output appears. If no 
output appears, there is a problem! All the issues I've encountered are due to 
a lack of power. Make sure each device has it's own wall outlet.

Final Equipment Setup:
======================
A. Raspberry Pi power supply (5V 1A or higher) with USB connection
B. 4GB or greater SD card
C. USB data cable connecting Raspberry Pi(L) to USB hub(H).
D. Ethernet port. Plug in Ethernet cord from here to modem. If using WiFi, leave port empty.
E. USB data cable connecting Phidgets board(J) to USB hub(H).
F. Power supply for USB hub (5V 4A for the one in the picture).
G. Power supply for Phidgets board (12V 2A).
H. USB hub
I. Phidgets sensors
J. Phidgets IO board
K. Mini USB WiFi dongle. Do not use if using direct Ethernet connection. Must be RTL8188CUS or RTL8192WiFi. Plugged into high-power port.
L. Raspberry Pi

.. image:: http://bitbucket.org/lucpervasiveseminar/environmental-monitoring/raw/master/images/enclosure.jpg

Please "View" the image to see a larger photo that can be zoomed in.

Cloning Raspbian image from SD card:
------------------------------------

Copying Raspbian image to new SD card:
--------------------------------------
