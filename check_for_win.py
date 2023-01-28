import pygame
from add_text import *


##############################################################################
#
#   Prints out the winner to the screen
#
def print_winner(winner, display):
    #   there was a winner
    if winner:
        # print('the winner is', winner)
        add_text(display, winner + ' has won!', 215, 550)    # display the winner with text
        return True                                          # return yes there was a winner
    else:
        return False


##############################################################################
#
#   Checks to see if a player won
#
#   Returns: if no one won then it returns false
#            if a player won it returns an 'X' or 'O' depending on who won
#
def check_for_win(status):

    winner = False

    #   check horizontals
    for i in range(3):
        if status.board[i][0] != 0 and status.board[i][0] == status.board[i][1] == status.board[i][2]:
            #   X won
            if status.board[i][0] == 1:
                winner = 'X'
                # print('X has won!')
            #   O won
            else:
                winner = 'O'
                # print('O has won!')

    #   check verticals
    for i in range(3):
        if status.board[0][i] != 0 and status.board[0][i] == status.board[1][i] == status.board[2][i]:
            #   X won
            if status.board[0][i] == 1:
                winner = 'X'
                # print('X has won!')
            #   O won
            else:
                winner = 'O'
                # print('O has won!')

    #   check diagnols
    if (status.board[0][0] != 0 and status.board[0][0] == status.board[1][1] == status.board[2][2]) or (
            0 != status.board[2][0] and status.board[1][1] == status.board[2][0] == status.board[0][2]):
        #   X won
        if status.board[1][1] == 1:
            winner = 'X'
            # print('X has won!')
        #   O won
        else:
            winner = 'O'
            # print('O has won!')

    return winner

