Raspberry pi/phidget setup:
===========================

Raspberry Pi Tutorial:
======================
1. Raspberry Pi OS Install (Raspbian). Skip this step if already using an SD card with Raspbian on it (provided by us, not a company).
#. Raspberry Pi Networking Setup. Cannot skip this step.
#. Raspberry Pi Software Install. Skip this step if using an SD card with software on it.
#. Final Equipment Setup

Raspberry Pi OS Install (Raspbian):
===================================

Equipment required:
-------------------
A. 1 USB hub
B. USB data cable for USB hub to raspberry pi (comes with USB hub)
C. raspberry pi
D. Raspberry Pi power supply (5V 1A or higher) with USB connection
E. 8GB or greater SD card
F. power supply for USB hub (comes with USB hub)  
G. ethernet cable connecting Raspberry Pi to router.
H. USB mouse
I. USB keyboard
J. HDMI cable (male to male).
K. Monitor or television with HDMI port.
L. Linux computer with SD card reader. Can be done on Windows, but you're on your own.

Instructions:
-------------
1. Insert blank SD card with at least 8GB capacity (E) into computer with SD card reader (L).
#. Take SD card and format it using "gparted" on a linux machine to format entire SD card as fat32. This can also be done on Windows, but you're on your own. 
#. Download NOOBS from http://www.raspberrypi.org/downloads and extract to SD card.
#. Connect USB hub (A) using data cable (B) to raspberry pi (C).
#. Insert SD card (E) into Raspberry Pi (C).
#. Connect power supply for USB hub (F) to USB hub (A). **Must be in it's own wall socket.**
#. Connect mouse and keyboard (H and I) to USB hub (A).
#. Connect monitor or television with HDMI port (K) to Raspberry Pi (C) via HDMI cable (J). Make sure you change your TV's input to HDMI.
#. Connect power supply for Raspberry Pi (D) into Raspberry Pi (C). **Must be in it's own wall socket.**
#. When the Raspberry Pi boots up, choose to install only Raspbian.

Raspberry Pi Networking Setup:
==============================

I assume here that you have either the same setup as when you installed
Raspbian (you just finished that step) or you have a final setup and you are 
adjusting an already working configuration (changing the IP address for
example).

First time networking users, run these commands to enable SSH::

    sudo apt-get install ssh
    sudo update-rc.d ssh defaults
    sudo reboot

On another computer already on the network, find the Bcast, Mask, and
appropriate inet address. This can be done on linux by the following
instructions::

    ifconfig

Write down inet addr, Bcast, and Mask for eth0. For example, my inet address
is 192.168.1.135, my Bcast address is 192.168.1.255, my Mask is 255.255.255.0

Now we need to find the Gateway and Destination addresses. On linux::

    netstat -nr

Write down Gateway address and Destination address. For example, my Gateway
address is 192.168.1.1 and my Destination address is 192.168.1.0

Now with this information, we can setup WiFi or Ethernet::

    sudo nano /etc/network/interfaces

Decide if you want to use Ethernet or WiFi and follow those instructions.

Ethernet:
---------

The file (/etc/network/interfaces) should read (replace the values with the 
values you wrote down previously, the values match my values previously)::

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

Run the following commands in a terminal::

    sudo reboot
    ping google.com

If the ping to google works, you have a working configuration!

See Port Forwarding section after WiFi.

WiFi (MUST use RTL8192CU or RTL8188CUS WiFi Adapter!):
------------------------------------------------------

The file (/etc/network/interfaces) should read (replace the values with the 
values you wrote down previously, the values match my values previously)::

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

Also edit the /etc/wpa_supplicant/wpa_supplicant.conf file (filling in your ssid and password. Some issues can occur if your ssid has spaces, so if you run into trouble, change your ssid to a single word to test)::

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="your_ssid"
        psk="your_password"
    }

Run the following commands in a terminal::

    sudo reboot
    ping google.com

If the ping to google works, you have a working configuration!

Port Forwarding (Do this after setting up WiFi or Ethernet):
------------------------------------------------------------
We need to forward the SSH port. These instructions are for Linksys routers.
1. Login to your router. (usually 192.168.1.1)
#. Look for the single port forwarding page.
#. Forward the external port 1990 to the internal port 22 (SSH port) with the IP address that you specified for the Raspberry Pi.
#. Save changes to your configuration on your router.
#. "sudo reboot" the Raspberry Pi. 
#. Test that this worked by doing::

    ssh -l pi -p 1990 <ip address>

Where <ip address> is your ROUTER's public IP address. Google "ip address" to find this information.

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

3. If you get any error like this::

    configure: error: "udev support requested but libudev not installed"
   
   install libudev::
    
    sudo apt-get install libudev-dev

    and go back to Step 2


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
a lack of power. **Make sure each powered device has it's own wall outlet.**

Final Equipment Setup:
======================
A. Raspberry Pi power supply (5V 1A or higher) with USB connector **plugged directly to wall socket.**
B. 8GB or greater SD card
C. USB data cable connecting Raspberry Pi(L) to USB hub(H).
D. Ethernet port. Plug in Ethernet cord from here to modem. If using WiFi, leave port empty.
E. USB data cable connecting Phidgets board(J) to USB hub(H).
F. Power supply for USB hub (5V 4A for the one in the picture) **plugged directly to wall socket.**
G. Power supply for Phidgets board (12V 2A) **plugged directly to wall socket.**
H. USB hub
I. Phidgets sensors
J. Phidgets IO board
K. Mini USB WiFi dongle. Do not use if using direct Ethernet connection. Must be RTL8188CUS or RTL8192WiFi. Plugged into high-power port.
L. Raspberry Pi

.. image:: http://bitbucket.org/lucpervasiveseminar/environmental-monitoring/raw/master/images/enclosure.jpg

Please "View" the image to see a larger photo that can be zoomed in.

Cloning Raspbian image from SD card:
------------------------------------

The purpose of cloning a Raspbian image from the SD card is to be able to take
a working configuration and then make "clones" of it for others to use. There
are some important things to note:

1. The image must be the smallest possible. This is because it is complicated to take a larger image and put it on a smaller SD card. To avoid this, keep the image size as small as possible. For example, use a 8GB SD card for your image. This way, others with 8GB SD cards or larger can use it.
2. Use a linux machine with an SD card reader to do your imaging. This cloning of the image can be done in one line on linux.
3. Make sure you test your image before you overwrite an old one in the repository! Copy the image to a new SD card and put it in the Raspberry Pi to test it.

Now, here are the steps to actually do it:

1. Put SD card with working Raspbian configuration of size 8GB into your SD card reader on your linux machine.
2. Run "sudo gparted".
3. In the gparted UI, on the top left is the menu GParted, click that and go to Devices.
4. You will see the name of your SD card there. For example, /dev/sdb2.
5. Run this command from a command line (replacing /dev/sdb2 with your name)::

    sudo dd if=/dev/sdb2 of=~/Desktop/raspberrypi.dmg

6. This will create the image on your Desktop called raspberrypi.dmg. This is your image. Running the command takes several minutes and shows no sign of progress until it is finished. **DO NOT CANCEL THIS COMMAND WHILE RUNNING OR YOU WILL CORRUPT YOUR SD CARD**.
#. If you corrupt your SD card, you can use the instructions in the next section to uncorrupt the SD card.
#. When it is finished, you will have your 8GB Raspberry Pi image. Commit this to the repository under /images

Copying Raspbian image to new SD card:
--------------------------------------

Here are the steps to clone the Raspbian image to an SD card:

1. Put ia blank SD card of size 8GB into your linux machine.
2. Run "sudo gparted".
3. In the gparted UI, on the top left is the menu GParted, click that and go to Devices.
4. You will see the name of your SD card there, click it.
5. Delete all partitions from this SD card.
6. Format the remaining unallocated space as fat32.
#. Click the Edit menu option and do "apply all"
#. After this is finished, you have a blank SD card formatted with fat32. Note the name of your SD card. For example, /dev/sdb2
#. Run this command from a command line (replacing /dev/sdb2 with your name)::

    sudo dd if=.../images/raspberrypi.dmg of=~/dev/sdb2

#. This will clone the raspberrypi image to your SD card. Running the command cah take almost an hour and shows no sign of progress until it is finished. **DO NOT CANCEL THIS COMMAND WHILE RUNNING OR YOU WILL CORRUPT YOUR SD CARD**.
#. If you corrupt your SD card, you can use gparted again to remove all partitions and format as fat32 again to try again.
#. When it is finished, you will have your 8GB Raspberry Pi image on your SD card.
