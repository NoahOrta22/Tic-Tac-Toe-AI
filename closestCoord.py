import math


#####################################################################
#
#   Finds out which box the mouse click was closest to
#
#   Returns: the box closest to the mouse click
#
def closestCoord(coordinates, pos):
    shortest = math.inf
    coord = []
    for i in range(3):
        for j in range(3):
            dis = math.dist(coordinates[i][j], pos)
            if dis < shortest:
                shortest = dis
                coord = [i, j]

    return coord[0], coord[1]
