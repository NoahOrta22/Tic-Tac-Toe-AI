from drawX import *
from drawO import *


def draw_shape(display, shape, coordinate):
    if shape == 'X':
        drawX(display, coordinate)
    elif shape == 'O':
        drawO(display, coordinate)
