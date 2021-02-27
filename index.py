import time
import datetime

from rpi_ws281x import Adafruit_NeoPixel, Color

from helpers import position, genereta_line

LED_WIDTH = 18
LED_HEIGHT = 14

LED_COUNT = 252
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 2
LED_INVERT = False

def loop(panel):
    for i in range(0, panel.numPixels(), 1):
        panel.setPixelColor(i, Color(170, 170, 170))
        time.sleep(0.1)
        panel.show()

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

    # for i in range(0, panel.numPixels(), 1):
        # panel.setPixelColor(i, Color(0, 100, 0))
        # panel.show()
    # while True:
    # genereta_line(panel, 0)
    # genereta_line(panel, 2)
    # genereta_line(panel, 4)
    # genereta_line(panel, 6)
    # genereta_line(panel, 8)
    # genereta_line(panel, 10)
    # genereta_line(panel, 12)
    # genereta_line(panel, 14)
    # genereta_line(panel, 16)

    genereta_line(panel, 1)
    genereta_line(panel, 3)
    genereta_line(panel, 5)
    genereta_line(panel, 7)
    genereta_line(panel, 9)
    genereta_line(panel, 11)
    genereta_line(panel, 13)
    genereta_line(panel, 15)
    genereta_line(panel, 17)
    # panel.show()
    # genereta_line(panel, 18)
        # genereta_line(panel, LED_HEIGHT, 1)
        # genereta_line(panel, LED_HEIGHT, 9)
    
        # time.sleep(0.1)
