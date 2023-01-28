# Importing the library
import pygame
import sys
from drawX import *
from drawO import *
from draw_shape import *
from closestCoord import *
from check_for_win import *
from add_text import *
from minimax import *

pygame.init()

#   Make the background
display = pygame.display.set_mode([450, 600])
color = (255, 255, 255)
display.fill(color)

#   Make the board
black = (0, 0, 0)
pygame.draw.line(display, black, (0, 150), (450, 150))
pygame.draw.line(display, black, (0, 300), (450, 300))
pygame.draw.line(display, black, (150, 0), (150, 450))
pygame.draw.line(display, black, (300, 0), (300, 450))
pygame.display.flip()

#   Make a matrix of center points of each position
coordinates = [[(75, 75), (225, 75), (375, 75)],
               [(75, 225), (225, 225), (375, 225)],
               [(75, 375), (225, 375), (375, 375)]]

#   Make a matrix to say whether board positions are available or not
#   (1 for X : -1 for O : 0 for unavailable)
blank_board = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]


class boardStatus():
    board: list
    plays: int

    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.plays = 0


status = boardStatus()

player_turn = True
winner = False
run = True
flag = True
reset_button = -1

player_num, opponent_num = 1, -1
player_letter, opponent_letter = 'X', 'O'

while run:
    #   Sleep the CPU for 0.3 seconds
    pygame.time.wait(300)

    # if the window exit button in pressed then shut down pygame
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    #   if the mouse is pressed down (clicked) and it's the PLAYERS TURN
    if events.type == pygame.MOUSEBUTTONUP and player_turn and not winner:
        ### I'll put an if statement if a user is playing
        x, y = pygame.mouse.get_pos()                   # find out where the mouse clicked
        ### then if it's the computer playing i'll have the computer give x and y here
        if y <= 450:                                    # make sure the click was in a box
            pos = (x, y)                                # put x & y coordinates in a tuple
            i, j = closestCoord(coordinates, pos)       # find out which square it's in
            if not status.board[i][j]:                  # check if it's available
                status.plays += 1                       # increment the amount of plays played

                draw_shape(display, player_letter, coordinates[i][j])
                player_turn = False                     # flip who's turn it is
                status.board[i][j] = player_num         # make that square unavailable, assign player_num for their shape

                # if player_turn:                         # check which players turn it is
                #     drawX(display, coordinates[i][j])   # draw a X
                #     player_turn = False                 # flip who's turn it is
                #     status.board[i][j] = 1              # make that square unavailable, assign 1 for X
                # else:
                #     drawO(display, coordinates[i][j])   # draw an O
                #     player_turn = True                  # flip who's turn it is
                #     status.board[i][j] = -1             # make that square unavailable, assign -1 for O

                winner = check_for_win(status)          # check for a winner

    #   THIS IS THE AI THAT IS PLAYING
    if not winner and not player_turn and status.plays != 9:
        coord, possible_outcomes = findBestMove(status)             # returns the best move
        a, b = coord
        print('possible outcomes: ', possible_outcomes)
        draw_shape(display, opponent_letter, coordinates[a][b])                # draw an O
        player_turn = True                                          # flip who's turn it is
        status.board[a][b] = opponent_num                                     # make that square unavailable, assign -1 for O
        status.plays += 1                                           # add to the # of plays that have been played
        winner = check_for_win(status)                              # check for a winner

    # there is a winner
    if winner and flag:
        # print_winner(winner, display)
        print(type(winner))
        add_text(display, winner + ' has won!', 215, 550)
        flag = False
        print(status.board)

    # it's a draw
    elif not winner and status.plays == 9 and flag:
        add_text(display, "It's a draw!", 215, 550)
        flag = False

    #   there was a win or draw
    if not flag:
        reset_button = add_text(display, "Reset", 400, 575, 35)

    # make the reset button pressable
    if events.type == pygame.MOUSEBUTTONUP and events.button == 1:
        print('game reset')

    #   update the screen
    pygame.display.update()
