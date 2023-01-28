import pygame


#   draws an X
def drawX(display, coordinate):
    top_left = (coordinate[0] - 30, coordinate[1] - 40)
    top_right = (coordinate[0] + 30, coordinate[1] - 40)
    bottom_left = (coordinate[0] - 30, coordinate[1] + 40)
    bottom_right = (coordinate[0] + 30, coordinate[1] + 40)

    black = (0, 0, 0)
    thickness = 3

    pygame.draw.line(display, black, top_left, bottom_right, thickness)
    pygame.draw.line(display, black, top_right, bottom_left, thickness)
    pygame.display.flip()
