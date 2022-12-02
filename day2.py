# day2.py

# --- IMPORTS ---
import os
import sys 

# --- CONSTANTS ---
INPUT_DIR = 'input/'
INPUT_FILE = 'day2-input.txt'

SHAPE_SCORE_ROCK = 1
SHAPE_SCORE_PAPER = 2
SHAPE_SCORE_SCISSORS = 3

OUTCOME_SCORE_LOST = 0
OUTCOME_SCORE_DRAW = 3
OUTCOME_SCORE_WON = 6

OPPONENT_MOVE_ROCK = 'A'
OPPONENT_MOVE_PAPER = 'B'
OPPONENT_MOVE_SCISSORS = 'C'

MY_MOVE_ROCK = 'X'
MY_MOVE_PAPER = 'Y'
MY_MOVE_SCISSORS = 'Z'

MOVE_NEED_TO_LOSE = 'X'
MOVE_NEED_TO_DRAW = 'Y'
MOVE_NEED_TO_WIN = 'Z'

OPPONENT_PLAYER = 0
MY_PLAYER = 1
MOVE_NEEDED_TO_MAKE = 1

def determine_move_score(my_move):
    if (my_move == MY_MOVE_ROCK):
        return SHAPE_SCORE_ROCK
    if (my_move == MY_MOVE_PAPER):
        return SHAPE_SCORE_PAPER
    if (my_move == MY_MOVE_SCISSORS):
        return SHAPE_SCORE_SCISSORS

def determine_outcome_score(opponent_move, my_move):
    # Compare Opponent Rock moves
    if (opponent_move == OPPONENT_MOVE_ROCK):
        if (my_move == MY_MOVE_ROCK):
            return OUTCOME_SCORE_DRAW
        if (my_move == MY_MOVE_PAPER):
            return OUTCOME_SCORE_WON
        if (my_move == MY_MOVE_SCISSORS):
            return OUTCOME_SCORE_LOST
    
    # Compare Opponent Paper moves
    if (opponent_move == OPPONENT_MOVE_PAPER):
        if (my_move == MY_MOVE_ROCK):
            return OUTCOME_SCORE_LOST
        if (my_move == MY_MOVE_PAPER):
            return OUTCOME_SCORE_DRAW 
        if (my_move == MY_MOVE_SCISSORS):
            return OUTCOME_SCORE_WON 
        
    # Compare Opponent Scissors moves
    if (opponent_move == OPPONENT_MOVE_SCISSORS):
        if (my_move == MY_MOVE_ROCK):
            return OUTCOME_SCORE_WON 
        if (my_move == MY_MOVE_PAPER):
            return OUTCOME_SCORE_LOST
        if (my_move == MY_MOVE_SCISSORS):
            return OUTCOME_SCORE_DRAW

def determine_curr_move_score(opponent_move, my_move):
    shape_score = determine_move_score(my_move)
    outcome_score = determine_outcome_score(opponent_move, my_move)

    return shape_score + outcome_score
        
def determine_total_score_strat_1(move_list):
    running_score = 0

    for move in move_list:
        move_score = determine_curr_move_score(move[OPPONENT_PLAYER], move[MY_PLAYER])

        running_score = running_score + move_score

    return running_score

def determine_move_to_make(opponent_move, move_to_make):
    # if the opponent plays Rock
    if (opponent_move == OPPONENT_MOVE_ROCK):
        if (move_to_make == MOVE_NEED_TO_LOSE):
            return MY_MOVE_SCISSORS
        if (move_to_make == MOVE_NEED_TO_DRAW):
            return MY_MOVE_ROCK
        if (move_to_make == MOVE_NEED_TO_WIN):
            return MY_MOVE_PAPER
        
    # if the opponent plays Paper
    if (opponent_move == OPPONENT_MOVE_PAPER):
        if (move_to_make == MOVE_NEED_TO_LOSE):
            return MY_MOVE_ROCK
        if (move_to_make == MOVE_NEED_TO_DRAW):
            return MY_MOVE_PAPER
        if (move_to_make == MOVE_NEED_TO_WIN):
            return MY_MOVE_SCISSORS
        
    # if the opponent plays Scissors 
    if (opponent_move == OPPONENT_MOVE_SCISSORS):
        if (move_to_make == MOVE_NEED_TO_LOSE):
            return MY_MOVE_PAPER
        if (move_to_make == MOVE_NEED_TO_DRAW):
            return MY_MOVE_SCISSORS
        if (move_to_make == MOVE_NEED_TO_WIN):
            return MY_MOVE_ROCK

def determine_total_score_strat_2(move_list):
    running_score = 0

    for move in move_list:
        my_move = determine_move_to_make(move[OPPONENT_PLAYER], move[MOVE_NEEDED_TO_MAKE])

        move_score = determine_curr_move_score(move[OPPONENT_PLAYER], my_move)

        running_score = running_score + move_score

    return running_score

def main():
    strategy_guide = []
    current_round = []

    path = os.path.join(os.getcwd(), INPUT_DIR, INPUT_FILE)

    input_file = open(path, 'r')

    for line in input_file:
        current_round = line.split()
        strategy_guide.append(current_round)

    print(determine_total_score_strat_1(strategy_guide))

    print(determine_total_score_strat_2(strategy_guide))

if __name__ == "__main__":
    main()