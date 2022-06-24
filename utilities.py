def compute_outcome(gameboard):
    for i in range(3):
        win = True
        lose = True
        for j in range(3):
            if gameboard[i][j] == 1 and win is True:
                win = True
            else:
                win = False
            if gameboard[i][j] == -1 and lose is True:
                lose = True
            else:
                lose = False
        if win is True or lose is True:
            break
    if win is True:
        return 1
    if lose is True:
        return -1

    for j in range(3):
        win = True
        lose = True
        for i in range(3):
            if gameboard[i][j] == 1 and win is True:
                win = True
            else:
                win = False
            if gameboard[i][j] == -1 and lose is True:
                lose = True
            else:
                lose = False
        if win is True or lose is True:
            break
    if win is True:
        return 1
    if lose is True:
        return -1

    win = True
    lose = True
    for i in range(3):
        if gameboard[i][i] == 1 and win is True:
            win = True
        else:
            win = False
        if gameboard[i][i] == -1 and lose is True:
            lose = True
        else:
            lose = False
    if win is True:
        return 1
    if lose is True:
        return -1

    win = True
    lose = True
    for i in range(3):
        if gameboard[2 - i][i] == 1 and win is True:
            win = True
        else:
            win = False
        if gameboard[2 - i][i] == -1 and lose is True:
            lose = True
        else:
            lose = False
    if win is True:
        return 1
    if lose is True:
        return -1

    return None


def print_gameboard(gameboard):
    for i in range(3):
        print(gameboard[i])
