"""
DC32 Badge Photoframe
"""

from lights import *
from screen import *
from read_sd_card_images import *
from buttons import *

def main():


    init_sd_card_images()
    init_lights()
    init_screen()
    rainbow_cycle(0)  # Increase the number to slow down the rainbow
         
main()
