
from machine import Pin
import neopixel
import time
import machine

num_pixels = 9
np = neopixel.NeoPixel(machine.Pin(4), num_pixels)
turn_lights_on = True

def toggle_lights_on():
    global turn_lights_on
    turn_lights_on = not turn_lights_on
    if (turn_lights_on):
        rainbow_cycle(0)
    
def stop_rainbow_cycle():
    turn_lights_on = False
    all_same_color((0,0,0))

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    while(turn_lights_on):
        for j in range(255):
            for i in range(num_pixels):
                rc_index = (i * 256 // num_pixels) + j
                np[i] = wheel(rc_index & 255)
            np.write()
            time.sleep(0.01)
            if (not turn_lights_on):
                break

def all_same_color(color):
    for i in range(num_pixels):
        np[i] = color
    np.write()

def demo(np):
    n = np.n

    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

def init_lights():
    # Initial colors
    np[0] = (255, 0, 0)
    np[1] = (255, 0, 0)
    np[2] = (255, 0, 0)
    np[3] = (255, 0, 0)
    np[4] = (255, 0, 0)
    np[5] = (255, 0, 0)
    np[6] = (255, 0, 0)
    np[7] = (255, 0, 0)
    np[8] = (255, 0, 0)
    np.write()