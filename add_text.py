import pygame


##############################################################################
#
#   Outputs text to the screen
#
#   input:  display - the screen object from pygame
#           string  - the text we want to output
#           x       - the x coordinate for the center of the text box
#           y       - the y coordinate for the center of the text box
#
def add_text(display, string, x, y, font_sz=50):
    black = (0, 0, 0)
    font = pygame.font.Font(None, font_sz)
    text = font.render(string, True, black)
    textRect = text.get_rect()
    textRect.center = (x, y)
    display.blit(text, textRect)
    # return display.blit(textRect, (x, y))
    # pygame.display.flip()

    # display.blit(text, (x, y))    # will fix this later to make the text a button
