from rpi_ws281x import Color

LED_WIDTH = 18
LED_HEIGHT = 14

COLOR_RED = Color(100,0,0)
COLOR_ORANGE = Color(200,100,0)
COLOR_YELLOW = Color(255,255,0)

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
    return int(x * LED_HEIGHT + (LED_HEIGHT - 1) - y) if not x % 2 else int(LED_HEIGHT * x + y)

def generate_color(max_height, led_position):
    delimiter = led_position / max_height

    if delimiter < 2/6:
        return COLOR_YELLOW
    elif delimiter < 4/6:
        return COLOR_ORANGE
    else:
        return COLOR_RED

def generate_line(panel, x, max_height):
    #  сначала очищаем линию по всей высоте
    for i in range(0, LED_HEIGHT, 1):
        panel.setPixelColor(position(x, i), Color(0, 0, 0))

    # затем ее перерисовываем
    for i in range(0, max_height, 1):
        panel.setPixelColor(position(x, i), generate_color(max_height, i))

    panel.show()
