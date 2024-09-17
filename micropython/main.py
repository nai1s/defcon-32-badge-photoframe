"""
DC32 Badge Photoframe
"""

from lights import *
from screen import *
from read_sd_card_images import *
from buttons import *
import asyncio

def main():


    init_sd_card_images()
    init_lights()
    init_screen()
    asyncio.run(rainbow_cycle(0))
         
main()
