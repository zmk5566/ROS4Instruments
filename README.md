# ROS2 Package for Sound and Music Instruments


This ROS2 package makes use of the powerful visualization tools, rosbags, and ros-topics to enable the use of sound and musical instruments. The package includes the following features:


**Serial2topic**: This tool converts serial input to rostopic messages.

**osc2topic**: This tool converts OSC (Open Sound Control) messages to ROS messages.

**topic2osc**: This tool subscribes to ROS topics and publishes them as OSC messages.

---------------------------------------
With these tools, you can easily integrate sound and music instruments with your ROS2 projects, and take advantage of the many benefits of the ROS2 ecosystem.

------------------------------

About Udev rules:

You might encounter udev issue while reading from serial. For the global udev rule inclusion for the system:

Do lsusb first to find our the idVendor and idProduct of the device:

    lsusb

I my case, I got:

    Bus 001 Device 009: ID 1a86:7523 QinHeng Electronics CH340 serial converter


They baseded on the response, I can create a custom rule in this file: **/etc/udev/rules.d/99-usb-serial.rules**

    SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7523",SYMLINK+="tty%E{ID_MODEL}"


Then reload this:

    $ udevadm control --reload
    $ reboot
