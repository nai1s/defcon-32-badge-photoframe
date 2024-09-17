from machine import Pin
from lights import all_same_color
from screen import *

def left_callback(p):
    display_next_image()
    all_same_color((255, 255, 0))

def right_callback(p):
    display_prev_image()
    all_same_color((0, 255, 255))

def a_callback(p):
    all_same_color((255, 0, 0))

def b_callback(p):
    all_same_color((0, 255, 255))

btn_left = Pin(19, Pin.IN, Pin.PULL_UP)
btn_right = Pin(16, Pin.IN, Pin.PULL_UP)
btn_a = Pin(21, Pin.IN, Pin.PULL_UP)
btn_b = Pin(20, Pin.IN, Pin.PULL_UP)

btn_left.irq(trigger=Pin.IRQ_FALLING, handler=left_callback)
btn_right.irq(trigger=Pin.IRQ_FALLING, handler=right_callback)
btn_a.irq(trigger=Pin.IRQ_FALLING, handler=a_callback)
btn_b.irq(trigger=Pin.IRQ_FALLING, handler=b_callback)

