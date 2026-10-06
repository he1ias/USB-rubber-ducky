from hsl import hsl_to_rgb

from machine import Pin
from neopixel import NeoPixel
import time

LED_COUNT = 5
LEVEL = 5

pixels = NeoPixel(Pin(28, Pin.OUT), LED_COUNT)
switch = Pin(27, Pin.IN, Pin.PULL_UP)
press = Pin(26, Pin.IN, Pin.PULL_UP)

count = 0
position = 0

last_press = 0

try:
    while True:
        now = time.ticks_ms()
        if switch.value() == 0 and now - last_press > 150:
            pixels[position] = (0, 0, 0)
            position = (position + 1) % LED_COUNT
            last_press = now
            
        if press.value() == 0:
            pixels.fill((0, LEVEL, 0))
        else:
            pixels.fill((0, 0, 0))
            pixels[position] = hsl_to_rgb(count, 100, LEVEL)

        pixels.write()
        time.sleep(0.05)
        count += 10
finally:
    pixels.fill((0, 0, 0))
    pixels.write()
