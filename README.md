# defcon-badge-photoframe
Photoframe showing images off an SD card using micropython on the DEFCON badge RP2350

Instructions are for a linux system, if you aren't using linux you may need to alter these steps.

# Flash the Badge Bootloader

In order to run the project you'll need to get the micropython firmware in place. I followed the steps from: [Micropython DC32](
https://github.com/p0ns/micropython-dc32) to produce the boatloader image micropython-dc32.uf2. You can flash this onto the hardware by:
1. Holding the "boot" button down
2. Press the "reset" button
3. Release the "boot" button

![badge buttons](images/badge%20buttons.jpg)

If your badge is on a USB-C connection, you should see a new device show up:
`RP2350`

if you run the `lsusb` command you'll see something like:  
`Bus 001 Device 011: ID 2e8a:000f Raspberry Pi RP2350 Boot`  



Copy the micropython firmware file into this device:  
`cp micropython-dc32.uf2 /media/[your user]/RP2350/`

You should see the device disconnect, if you run `lsusb` you'll now get:  
`Bus 001 Device 012: ID 2e8a:0005 MicroPython Board in FS mode`

# Load Micropython Code

Install [Thonny](https://thonny.org/) and open it to your code folder. Go to `Tools > Options` and open the `Interpreters` Tab, if everything is configured you should see the Raspberry Pi in the list of devices:
![Thonny Config](images/Thonny%20Config.png)


Then, select all the .py files from this repo and right click to upload them to the device. I ran into a permissions error that I had to fix before the device would recognize/execute:  
`sudo usermod -a -G dialout ihs`

# Setup an SD Card

Format an SD Card as FAT. I had to use a new one, unfortunately the DEFCON32 badge sd card kept giving me read errors. Once you have it formatted, put as many images as you like on the card - these should be 320 x 240 pixels. Insert the SD Card into the badge, start it up and you should see images loading!

# Controls

| Key | Action |
| --- | ----- |
| Left | Previous Image |
| Right | Next Image |
| Up | Slideshow |
| Down | Change LED Pattern |

# Future Work

I'd like to use this project as a starting point for defcon-photobbomb, but I'm stuck on the IR controls. If you want to contribute please try out that repo!
