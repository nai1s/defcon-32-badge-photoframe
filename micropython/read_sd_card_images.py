import machine
import sdcard
import uos

# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(13, machine.Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(14),
                  mosi=machine.Pin(15),
                  miso=machine.Pin(12))
error_during_sd_read = False
try:
    # Initialize SD card
    sd = sdcard.SDCard(spi, cs)
 
    # Mount filesystem
    vfs = uos.VfsFat(sd)
    sd_dir = '/sd'
    uos.mount(vfs, sd_dir)
except Exception as e:
    print(e)
    error_during_sd_read = True

sd_dir = '/sd/'
current_image = -1
error_image = 'no_images_found.png'

def init_sd_card_images():
    global current_image
    current_image = 1

def get_sd_card_image_list():
    available_images = uos.listdir(sd_dir)
    if (len(available_images) < 1):
        raise "no images found"
    else:
        return available_images

def get_prev_image():
    if (error_during_sd_read):
        return error_image
    try:
        global current_image
        available_images = get_sd_card_image_list()
        current_image = current_image - 1
        if (current_image < 0):
            current_image = len(available_images) - 1
        return sd_dir + available_images[current_image]
    except:
        return error_image

def get_next_image():
    if (error_during_sd_read):
        return error_image
    try:
        global current_image
        available_images = get_sd_card_image_list()
        current_image = current_image + 1
        if (current_image > len(available_images) - 1):
            current_image = 0
        return sd_dir + available_images[current_image]
    except:
        return error_image