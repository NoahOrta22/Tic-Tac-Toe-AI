import pygame


#   draws an O
def drawO(display, coordinate):
    black = (0, 0, 0)
    radius = 45
    thickness = 3
    pygame.draw.circle(display, black, coordinate, radius, thickness)
    pygame.display.flip()
