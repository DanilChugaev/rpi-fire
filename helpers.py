from rpi_ws281x import Color

LED_WIDTH = 18
LED_HEIGHT = 14

def position(x = 0, y = 0):
    """
    Определяет местоположение светодиода по указанным координатам
    Нечетные полосы (начиная от 0 светодиода) идут вниз
    Четные идут вверх

    Keyword arguments:
    x -- позиция по оси `x` (default 0)
    y -- позиция по оси `y` (default 0)

    Returns:
    number -- итоговая позиция светодиода
    """
    # return int(x * 14 + y) if not x % 2 else int((x - ((x-1)/2)) * 14 * 2 - 1 - y)
    # return int(x * LED_HEIGHT + (LED_HEIGHT - 1) - y)
    return int((x - ((x-1)/2)) * LED_HEIGHT * 2 - 1 - y)

def genereta_line(panel, x):
    for i in range(0, LED_HEIGHT, 1):
        # print(i)
        panel.setPixelColor(position(x, i), Color(150, 0, 0))
        panel.show()