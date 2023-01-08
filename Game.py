from constants import *
import copy
import math

whose_turn = -1 # 1 represents white and -1 represents black

def change_turn():
    global whose_turn
    whose_turn = -whose_turn

def successor(state, turn):
    """
    returns a list of states that can be reached by taking a legal action
    """
    output = []

    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '-':
                continue
            
            new_state = play(state, i, j, turn)
            if new_state != None:
                output.append(new_state)

    return output

def play(state, i, j, turn):
    """
    returns None if player can't play that position 
    or returns a new state made by playing that position
    """
    can_place = False
    new_state = copy.deepcopy(state)

    enemy_color = 'B' if turn == 1 else 'W'
    friendly_color = 'W' if turn == 1 else 'B'

    for dir in Directions:
        if dtff(state, i, j, dir, turn) <= 1.5:
            continue
        can_place = True

        new_state[i][j] = friendly_color

        scan_row = i + dir[0]
        scan_col = j + dir[1]
        while new_state[scan_row][scan_col] == enemy_color:
            new_state[scan_row][scan_col] = friendly_color
            scan_row = scan_row + dir[0]
            scan_col = scan_col + dir[1]
            
    if not can_place:
        return None
    return new_state

def dtff(state, i, j, dir, turn):
    """
    'distance to first friendly color' in the specified direction; returns -1 if 
    there is no friendly color in that direction or reachs empty cell first;
    """
    enemy_color = 'B' if turn == 1 else 'W'
    friendly_color = 'W' if turn == 1 else 'B'

    scan_row = i + dir[0]
    scan_col = j + dir[1]
    while True:
        if scan_row < 0 or scan_row >= len(state):
            return -1
        if scan_col < 0 or scan_col >= len(state[0]):
            return -1
        if state[scan_row][scan_col] == '-':
            return -1
        if state[scan_row][scan_col] == friendly_color:
            return math.sqrt((scan_row - i)**2 + (scan_col - j)**2)
        if state[scan_row][scan_col] == enemy_color:
            scan_row = scan_row + dir[0]
            scan_col = scan_col + dir[1]
    

def is_terminal(state):
    """
    checks to see if the game is over or not
    """
    res = True
    for row in state:
        for cell in row:
            if cell == '-':
                res = False
    return res

def display(state):
    print("---------------------------------------")
    for row in state:
        print(" ".join(row))
    print("---------------------------------------")

def showResult(state):
    white_num = 0
    black_num = 0
    for row in state:
        for cell in row:
            if cell == 'W':
                white_num += 1
            if cell == 'B':
                black_num += 1
    print("---------------------------------------")
    print("number of white stones: ", white_num)
    print("number of black stones: ", black_num)
    print()
    if white_num > black_num:
        print("the winner is white!")
    elif white_num < black_num:
        print("the winner is black!")
    else:
        print("draw!")
    print("---------------------------------------")