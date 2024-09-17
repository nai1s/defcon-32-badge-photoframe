from machine import Pin
from screen import *
from lights import *


def left_callback(p):
    display_next_image()

def right_callback(p):
    display_prev_image()

def a_callback(p):
    #This is hacky, there are two while loops defined so for now just stop cycling the lights
    stop_rainbow_cycle()
    toggle_slideshow_mode()

def b_callback(p):
    stop_slideshow()
    toggle_lights_on()

btn_left = Pin(19, Pin.IN, Pin.PULL_UP)
btn_right = Pin(16, Pin.IN, Pin.PULL_UP)
btn_a = Pin(21, Pin.IN, Pin.PULL_UP)
btn_b = Pin(20, Pin.IN, Pin.PULL_UP)

btn_left.irq(trigger=Pin.IRQ_FALLING, handler=left_callback)
btn_right.irq(trigger=Pin.IRQ_FALLING, handler=right_callback)
btn_a.irq(trigger=Pin.IRQ_FALLING, handler=a_callback)
btn_b.irq(trigger=Pin.IRQ_FALLING, handler=b_callback)

