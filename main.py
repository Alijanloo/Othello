import Game
from constants import *
from algorithms import minMaxSearch, AlphaBetaPruning, BeamSearch
from time import time

def main():

    input = open(Input_path, 'r')

    initial_state = []
    while True:
        line = input.readline()
        if len(line) == 0:
            break
        initial_state.append(line.split())
    
    state = initial_state
    hadAction = False # keep track to notice when there wasn't any action for two turn, then the game will be over

    start_time = time()
    while not Game.is_terminal(state):
        HasAction = False

        childs = Game.successor(state, Game.whose_turn)

        if len(childs) > 0:
            HasAction = True
            hadAction = True
        if not HasAction:
            print("there is no possible action; skipping...")
            if not hadAction:
                break
            else:
                hadAction = False

        # try to maximize state value for white
        if Game.whose_turn == 1:
            best_choice = float('-inf')

            for child in childs:
                score = AlphaBetaPruning(child, False, 3, float('-inf'), float('inf'))
                # print(score)
                if score >= best_choice:
                    best_choice = score
                    state = child
        # try to minimize state value for black
        else:
            best_choice = float('inf')

            for child in childs:
                score = AlphaBetaPruning(child, True, 3, float('-inf'), float('inf'))
                # print(score)
                if score <= best_choice:
                    best_choice = score
                    state = child

        Game.change_turn()
        Game.display(state)
    
    Game.showResult(state)
    print(time() - start_time)

main()