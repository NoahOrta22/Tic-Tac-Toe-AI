from check_for_win import check_for_win

player, opponent = -1, 1
player_letter, opponent_letter = 'O', 'X'


def minimax(status, depth, maximizing, alpha=-100, beta=100, possible_outcomes=0):

    winner = check_for_win(status)                                #   check if that position has a winning outcome
    if winner == player_letter:                                   #   X won
        return 10, possible_outcomes
    elif winner == opponent_letter:                               #   O won
        return -10, possible_outcomes
    elif status.plays == 9:                                       #   it's a draw
        return 0, possible_outcomes

    #   if it's the maximizer's turn
    if maximizing:
        best = -1000

        #   loop through possible game plays
        for i in range(3):
            for j in range(3):

                if not status.board[i][j]:                        #   if the space is available
                    possible_outcomes += 1
                    status.plays += 1
                    status.board[i][j] = player                        #   X's turn, add a 1

                    score, possible_outcomes = minimax(status, depth + 1, not maximizing, alpha, beta, possible_outcomes)
                    best = max(best, score)
                    alpha = max(alpha, best)

                    status.board[i][j] = 0                        # undo the move
                    status.plays -= 1

                    # Alpha Beta Pruning
                    if beta <= alpha:
                        break

        return best, possible_outcomes

    #   if it's the minimizer's turn
    else:
        best = 1000

        #   loop through possible game plays
        for i in range(3):
            for j in range(3):

                if not status.board[i][j]:               # if the space is available
                    possible_outcomes += 1
                    status.plays += 1
                    status.board[i][j] = opponent        # opponent's turn

                    score, possible_outcomes = minimax(status, depth + 1, not maximizing, alpha, beta, possible_outcomes)
                    best = min(best, score)
                    beta = min(beta, best)

                    status.board[i][j] = 0               # undo the move
                    status.plays -= 1

                    # Alpha Beta Pruning
                    if beta <= alpha:
                        break

        return best, possible_outcomes


def findBestMove(status):
    best_val = -1000
    best_move = (-1, -1)
    possible_outcomes = 0
    best_depth = 10


    #   loop through possible game plays
    for i in range(3):
        for j in range(3):
            if not status.board[i][j]:                # if the space is available

                status.plays += 1
                status.board[i][j] = player           # player's turn

                move_val, temp_moves = minimax(status, 0, False)  # compute evaluation function for this move
                possible_outcomes += temp_moves
                status.plays -= 1

                status.board[i][j] = 0                # undo the move

                if move_val >=best_val:  # if the value of the current move is more than the best
                    best_move = (i, j)                # more than the best value, then update best
                    best_val = move_val

    return best_move, possible_outcomes
