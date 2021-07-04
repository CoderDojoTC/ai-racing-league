Logitec F710 Game Controller for DonkeyCar

https://docs.donkeycar.com/parts/controllers/

Testing to see if the Nano Recognizes the F710 USB Dongle
You can use the "lsusb" UNIX shell command to list all the USB devices:

$ lsusb
Bus 002 Device 002: ID 0bda:0411 Realtek Semiconductor Corp. 
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 004: ID 0bda:8179 Realtek Semiconductor Corp. RTL8188EUS 802.11n Wireless Network Adapter
Bus 001 Device 005: ID 046d:c21f Logitech, Inc. F710 Wireless Gamepad [XInput Mode]
Bus 001 Device 002: ID 0bda:5411 Realtek Semiconductor Corp. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

Note that the USB device with an ID of 046d:c21f has been found in the 4th line above.  The first ID before the colon is the device manufacturer (Logiteh) and the second is the id of their device (c21f).  Linux looks this number up in their system and then loads the driver for this type of device.

The driver will create a device file in the /dev/input directory called js0

$ ls -l /dev/input/js0
crw-rw-r--+ 1 root input 13, 0 Aug 16 19:30 /dev/input/js0

The "c" in the first letter says that this is a character I/O device.


$ sudo apt-get install evtest
[sudo] password for dan: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  apt-clone archdetect-deb bogl-bterm busybox-static cryptsetup-bin dpkg-repack gir1.2-timezonemap-1.0 gir1.2-xkl-1.0
  grub-common kde-window-manager kinit kio kpackagetool5 kwayland-data kwin-common kwin-data kwin-x11 libdebian-installer4
  libkdecorations2-5v5 libkdecorations2private5v5 libkf5activities5 libkf5attica5 libkf5completion-data libkf5completion5
  libkf5declarative-data libkf5declarative5 libkf5doctools5 libkf5globalaccel-data libkf5globalaccel5
  libkf5globalaccelprivate5 libkf5idletime5 libkf5jobwidgets-data libkf5jobwidgets5 libkf5kcmutils-data libkf5kcmutils5
  libkf5kiocore5 libkf5kiontlm5 libkf5kiowidgets5 libkf5newstuff-data libkf5newstuff5 libkf5newstuffcore5 libkf5package-data
  libkf5package5 libkf5plasma5 libkf5quickaddons5 libkf5solid5 libkf5solid5-data libkf5sonnet5-data libkf5sonnetcore5
  libkf5sonnetui5 libkf5textwidgets-data libkf5textwidgets5 libkf5waylandclient5 libkf5waylandserver5 libkf5xmlgui-bin
  libkf5xmlgui-data libkf5xmlgui5 libkscreenlocker5 libkwin4-effect-builtins1 libkwineffects11 libkwinglutils11
  libkwinxrenderutils11 libqgsttools-p1 libqt5designer5 libqt5help5 libqt5multimedia5 libqt5multimedia5-plugins
  libqt5multimediaquick-p5 libqt5multimediawidgets5 libqt5opengl5 libqt5positioning5 libqt5printsupport5 libqt5qml5
  libqt5quick5 libqt5quickwidgets5 libqt5sensors5 libqt5sql5 libqt5test5 libqt5webchannel5 libqt5webkit5 libxcb-composite0
  libxcb-cursor0 libxcb-damage0 os-prober python3-dbus.mainloop.pyqt5 python3-icu python3-pam python3-pyqt5
  python3-pyqt5.qtsvg python3-pyqt5.qtwebkit python3-sip qml-module-org-kde-kquickcontrolsaddons qml-module-qtmultimedia
  qml-module-qtquick2 rdate tasksel tasksel-data
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  evemu-tools libevemu3
The following NEW packages will be installed:
  evemu-tools evtest libevemu3
0 upgraded, 3 newly installed, 0 to remove and 7 not upgraded.
Need to get 38.2 kB of archives.
After this operation, 191 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ports.ubuntu.com/ubuntu-ports bionic/universe arm64 libevemu3 arm64 2.6.0-0.1 [11.0 kB]
Get:2 http://ports.ubuntu.com/ubuntu-ports bionic/universe arm64 evemu-tools arm64 2.6.0-0.1 [12.3 kB]
Get:3 http://ports.ubuntu.com/ubuntu-ports bionic/universe arm64 evtest arm64 1:1.33-1build1 [14.9 kB]
Fetched 38.2 kB in 1s (56.1 kB/s) 
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package libevemu3:arm64.
(Reading database ... 140149 files and directories currently installed.)
Preparing to unpack .../libevemu3_2.6.0-0.1_arm64.deb ...
Unpacking libevemu3:arm64 (2.6.0-0.1) ...
Selecting previously unselected package evemu-tools.
Preparing to unpack .../evemu-tools_2.6.0-0.1_arm64.deb ...
Unpacking evemu-tools (2.6.0-0.1) ...
Selecting previously unselected package evtest.
Preparing to unpack .../evtest_1%3a1.33-1build1_arm64.deb ...
Unpacking evtest (1:1.33-1build1) ...
Setting up evtest (1:1.33-1build1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Setting up libevemu3:arm64 (2.6.0-0.1) ...
Setting up evemu-tools (2.6.0-0.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
dan@danm-nano:~$ 

Now run it:

$ evtest

No device specified, trying to scan all of /dev/input/event*
Not running as root, no devices may be available.
Available devices:
/dev/input/event2:	Logitech Gamepad F710

Select the device event number [0-2]: 2

Logitech Gamepad F710 Input driver version is 1.0.1
Input device ID: bus 0x3 vendor 0x46d product 0xc21f version 0x305
Input device name: "Logitech Gamepad F710"
Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
    Event code 304 (BTN_SOUTH)
    Event code 305 (BTN_EAST)
    Event code 307 (BTN_NORTH)
    Event code 308 (BTN_WEST)
    Event code 310 (BTN_TL)
    Event code 311 (BTN_TR)
    Event code 314 (BTN_SELECT)
    Event code 315 (BTN_START)
    Event code 316 (BTN_MODE)
    Event code 317 (BTN_THUMBL)
    Event code 318 (BTN_THUMBR)
  Event type 3 (EV_ABS)
    Event code 0 (ABS_X)
      Value    128
      Min   -32768
      Max    32767
      Fuzz      16
      Flat     128
    Event code 1 (ABS_Y)
      Value   -129
      Min   -32768
      Max    32767
      Fuzz      16
      Flat     128
    Event code 2 (ABS_Z)
      Value      0
      Min        0
      Max      255
    Event code 3 (ABS_RX)
      Value    128
      Min   -32768
      Max    32767
      Fuzz      16
      Flat     128
    Event code 4 (ABS_RY)
      Value   -129
      Min   -32768
      Max    32767
      Fuzz      16
      Flat     128
    Event code 5 (ABS_RZ)
      Value      0
      Min        0
      Max      255
    Event code 16 (ABS_HAT0X)
      Value      0
      Min       -1
      Max        1
    Event code 17 (ABS_HAT0Y)
      Value      0
      Min       -1
      Max        1
Properties:
Testing ... (interrupt to exit)

Now as you press any key or move any joystick you will see the events.

When I press the yellow Y we see:
Event: time 1566006064.962158, type 1 (EV_KEY), code 308 (BTN_WEST), value 1
Event: time 1566006064.962158, -------------- SYN_REPORT ------------
Event: time 1566006065.129981, type 1 (EV_KEY), code 308 (BTN_WEST), value 0
Event: time 1566006065.129981, -------------- SYN_REPORT ------------

Blue X
Event: time 1566006110.047015, type 1 (EV_KEY), code 307 (BTN_NORTH), value 1
Event: time 1566006110.047015, -------------- SYN_REPORT ------------
Event: time 1566006110.182606, type 1 (EV_KEY), code 307 (BTN_NORTH), value 0
Event: time 1566006110.182606, -------------- SYN_REPORT ------------

Red B
Event: time 1566006143.423217, type 1 (EV_KEY), code 305 (BTN_EAST), value 1
Event: time 1566006143.423217, -------------- SYN_REPORT ------------
Event: time 1566006143.499642, type 1 (EV_KEY), code 305 (BTN_EAST), value 0
Event: time 1566006143.499642, -------------- SYN_REPORT ------------

Green A
Event: time 1566006184.060282, type 1 (EV_KEY), code 304 (BTN_SOUTH), value 1
Event: time 1566006184.060282, -------------- SYN_REPORT ------------
Event: time 1566006184.128408, type 1 (EV_KEY), code 304 (BTN_SOUTH), value 0
Event: time 1566006184.128408, -------------- SYN_REPORT ------------

Moving the joystick generates:
Event: time 1566006255.549652, -------------- SYN_REPORT ------------
Event: time 1566006255.553650, type 3 (EV_ABS), code 1 (ABS_Y), value -10923
Event: time 1566006255.553650, -------------- SYN_REPORT ------------
Event: time 1566006255.557650, type 3 (EV_ABS), code 1 (ABS_Y), value -14264
Event: time 1566006255.557650, -------------- SYN_REPORT ------------
Event: time 1566006255.561652, type 3 (EV_ABS), code 1 (ABS_Y), value -18633





