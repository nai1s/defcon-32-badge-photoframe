"""
ST7789 example for DC32 badge
"""

from lights import *
from buttons import *
from screen import *
from read_sd_card_images import *

def main():


    init_sd_card_images()
    init_lights()
    all_same_color((0, 255, 0))
    init_screen()
   #while(True):
   #     rainbow_cycle(0)  # Increase the number to slow down the rainbow

main()
