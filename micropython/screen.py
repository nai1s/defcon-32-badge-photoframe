import st7789
import tft_config
from screen import *
from read_sd_card_images import *
import time


tft = tft_config.config(3, buffer_size=4096) #rotation 3 for normal orientation, 1 for upside down

slideshow_mode = False

def stop_slideshow():
    slideshow_mode = False

def init_screen():
    png_file_name = get_next_image()
    tft.init()
    print(f'Displaying {png_file_name}')
    tft.png(png_file_name, 0, 0)
    
def display_next_image():
    png_file_name = get_next_image()
    print(f'Displaying {png_file_name}')
    tft.png(png_file_name, 0, 0)

def display_prev_image():
    png_file_name = get_prev_image()
    tft.png(png_file_name, 0, 0)   
    
def slideshow():
    while (slideshow_mode):
        display_next_image()
        time.sleep(10)
    
    
def toggle_slideshow_mode():
    global slideshow_mode
    slideshow_mode = not slideshow_mode
    print(f'Slideshow mode {slideshow_mode}')
    if (slideshow_mode):
        slideshow()
    