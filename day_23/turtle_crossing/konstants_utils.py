from random import randint

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480


def random_color_hex():
    return f'#{hex(randint(16, 255))[2:]}{hex(randint(16, 255))[2:]}{hex(randint(16, 255))[2:]}'
