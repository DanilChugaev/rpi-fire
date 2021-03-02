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
LED_BRIGHTNESS = 90
LED_INVERT = False

MIN_HEIGHT = 3
# создаем массив для хранения высот линий
height_list = [MIN_HEIGHT] * LED_WIDTH

def loop(panel):
    for i in range(0, LED_WIDTH, 1):
        min_height = MIN_HEIGHT if height_list[i] - 3 <= MIN_HEIGHT else height_list[i] - 3
        max_height = LED_HEIGHT if height_list[i] + 3 >= LED_HEIGHT else height_list[i] + 3
        height = int(random.uniform(min_height, max_height))
        height_list[i] = height

        generate_line(panel, i, height)

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
