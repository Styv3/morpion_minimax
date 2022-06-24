from copy import deepcopy
from utilities import compute_outcome, print_gameboard


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.outcome = None

    def __repr__(self):
        return f"{{val: {self.val}, children: [...], outcome: {self.outcome}\n}}"


node = Node([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
pturn = 1


def generate_children(node, pturn):
    ex_aequo = True
    for i in range(3):
        for j in range(3):
            if node.val[i][j] == 0:
                ex_aequo = False
                child = Node(deepcopy(node.val))
                child.val[i][j] = pturn
                node.children.append(child)
                outcome = compute_outcome(child.val)
                if outcome is not None:
                    child.outcome = outcome
                else:
                    generate_children(child, -pturn)
    if ex_aequo is True:
        node.outcome = 0


def minimax(node, pturn):
    if len(node.children) == 0:
        return node.outcome
    if pturn == 1:
        node.outcome = float("-inf")
    elif pturn == -1:
        outcome = float("+inf")
        for child in node.children:
            outcome = min(outcome, child.outcome)
    return outcome


def game():
    endgame = False
    current_player = 1
    gameboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    turn = 0

    while endgame is False:
        turn += 1
        print_gameboard(gameboard)
        if current_player == 1:
            pas_bon = True
            while pas_bon is True:
                try:
                    pplay = int(input("Choisissez votre case !"))
                    pas_bon = False
                except ValueError:
                    pas_bon = True
        elif current_player == -1:
            pas_bon = True
            while pas_bon is True:
                try:
                    pplay = int(input("Futur IA: Choisissez votre case !"))
                    pas_bon = False
                except ValueError:
                    pas_bon = True

        for i in range(3):
            for j in range(3):
                if pplay == i * 3 + j + 1 and gameboard[i][j] == 0:
                    gameboard[i][j] = current_player

        if compute_outcome(gameboard) is not None:
            print_gameboard(gameboard)
            print(f"{current_player} won")
            endgame = True
        if turn == 9:
            print_gameboard(gameboard)
            print(f"No one won")
            endgame = True

        current_player = -current_player


game()

"""        if pplay == 1 and node.val[2][0] == 0:
            node.val[2][0] = 1
        if pplay == 2 and node.val[2][1] == 0:
            node.val[2][1] = 1
        if pplay == 3 and node.val[2][2] == 0:
            node.val[2][2] = 1
        if pplay == 4 and node.val[1][0] == 0:
            node.val[1][0] = 1
        if pplay == 5 and node.val[1][1] == 0:
            node.val[1][1] = 1
        if pplay == 6 and node.val[1][2] == 0:
            node.val[1][2] = 1
        if pplay == 7 and node.val[0][0] == 0:
            node.val[0][0] = 1
        if pplay == 8 and node.val[0][1] == 0:
            node.val[0][1] = 1
        if pplay == 9 and node.val[0][2] == 0:
            node.val[0][2] = 1"""
