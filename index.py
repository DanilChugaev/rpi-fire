import time
import datetime
import random

from rpi_ws281x import Adafruit_NeoPixel, Color

from helpers import position, generate_line

LED_WIDTH = 18
LED_HEIGHT = 14
TIME_SLEEP = 0.001

LED_COUNT = 252
LED_PIN = 18
LED_FREQ_HZ = 900000
LED_DMA = 10
LED_BRIGHTNESS = 2
LED_INVERT = False

def loop(panel):
    for i in range(0, LED_WIDTH, 1):
        generate_line(panel, i, int(random.uniform(1, LED_HEIGHT)))

    time.sleep(TIME_SLEEP)

if __name__ == '__main__':
    panel = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
    )

    panel.begin()

    while True:
        loop(panel)
