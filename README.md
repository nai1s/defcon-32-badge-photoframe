# DEFCon Badge Photoframe
Photoframe showing images off an SD card using micropython on the DEFCON badge RP2350

Instructions are for a linux system, if you aren't using linux you may need to alter these steps.

# Flash the Badge Bootloader

In order to run the project you'll need to get the micropython firmware in place. I followed the steps from [Micropython DC32](
https://github.com/p0ns/micropython-dc32) to compile the boatloader image micropython-dc32.uf2. You can flash this onto the hardware by:
1. Hold the "boot" button down
2. Press the "reset" button
3. Release the "boot" button

![badge buttons](images/badge%20buttons.jpg)

If your badge is on a USB-C connection, you should see a new device show up:
`RP2350`

if you run the `lsusb` command you'll see something like:  
`Bus 001 Device 011: ID 2e8a:000f Raspberry Pi RP2350 Boot`  



Copy the micropython firmware file onto this device:  
`cp micropython-dc32.uf2 /media/[your user]/RP2350/`

You should see the device disconnect, if you run `lsusb` you'll now get:  
`Bus 001 Device 012: ID 2e8a:0005 MicroPython Board in FS mode`

# Load Micropython Code

Install [Thonny](https://thonny.org/) and open it to your code folder. Go to `Tools > Options` and open the `Interpreters` Tab, if everything is configured you should see the Raspberry Pi in the list of devices:
![Thonny Config](images/Thonny%20Config.png)

After you select it, you should see a python shell open to the device:  
``
MicroPython v1.23.0-319.g8a14546c2 on 2024-09-14; Raspberry Pi Pico2 with RP2350.
``


Then, select all the files from the `micropython` folder and right click to upload them to the device. I ran into a permissions error that I had to fix before the device would recognize/execute code:  
`sudo usermod -a -G dialout ihs`

After that you should be able to start the photoframe by unplugging the USB-C cable and restarting the badge or by running `main.py`.

# Setup an SD Card

Format an SD Card as FAT. I had to use a new one, unfortunately the DEFCON32 badge sd card kept giving me read errors. Once you have it formatted, put as many images as you like on the card - these should be 320 x 240 pixels. Insert the SD Card into the badge, start it up and you should see images loading!

# Controls

| Key | Action |
| --- | ----- |
| Left | Previous Image |
| Right | Next Image |
| A | Slideshow |
| B | Change LED Pattern |

# Future Work

Currently the slideshow is buggy, once you start it you can't stop. Rewriting the lights/screenshow to better use asynchronous methods and/or a central game loop would help.

I'd like to use this project as a starting point for [DEFCON photobbomb](https://github.com/nai1s/defcon-badge-photobomb), but I'm stuck on the IR controls. If you want to contribute please try out that repo!
