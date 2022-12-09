# day5.py

# -- IMPORTS --
import os 
import sys

# -- CONSTANTS --
INPUT_DIR = 'input/'
INPUT_FILE = 'day5-input.txt'

INDEX_CRATES_TO_MOVE = 0
INDEX_STACK_SRC = 1
INDEX_STACK_DST = 2

INDEX_TOKEN_NUM_OF_CRATES = 1
INDEX_TOKEN_SRC_STACK = 3
INDEX_TOKEN_DST_STACK = 5

def populate_empty_crates(input):
    index = 1
    increment_value = 4
    crate_contents = []
    
    while index < (len(input) - 1):
        crate_contents.append(input[index])
        index = index + increment_value

    return crate_contents

def create_arrangement_dict(raw_input):
    supplies = []

    last_line = ''
    index = 0

    last_line_index = len(raw_input) - 1
    last_line = raw_input[last_line_index].strip()

    total_num_of_stacks = last_line.split(' ')[-1]
    total_num_of_stacks = int(total_num_of_stacks)

    # create stacks
    for i in range(0, total_num_of_stacks):
        crates_in_stack = []
        supplies.append(crates_in_stack)

    # Don't parse the last row since the raw input only includes indices
    # and not the actual crate positions
    for i in range(last_line_index - 1, -1, -1):
        crates = populate_empty_crates(raw_input[i])

        for j in range(0, total_num_of_stacks):
            crate_contents = crates[j].strip()

            if not (crate_contents == ''):
                supplies[j].append(crate_contents)
    
    return supplies

def create_move_dict(raw_input):
    move_dict = []
    current_move = []

    for line in raw_input:
        tokens = line.split(' ')

        # first number: amount of crates to move at once
        current_move.append(int(tokens[INDEX_TOKEN_NUM_OF_CRATES]))

        # second number: source stack #
        current_move.append(int(tokens[INDEX_TOKEN_SRC_STACK]))

        # third number: destiation stack #
        current_move.append(int(tokens[INDEX_TOKEN_DST_STACK]))

        # Append current move to move dictionary
        move_dict.append(current_move)

        # Reset values
        current_move = []

    return move_dict        

def simulate_result(arrangement, moves, maintain_order):
    crate_holding = []

    for move in moves:
        src_stack = move[INDEX_STACK_SRC] - 1
        num_of_crates_to_move = move[INDEX_CRATES_TO_MOVE]

        # dequeue crates from source
        crate_holding = arrangement[src_stack][-num_of_crates_to_move:]
        arrangement[src_stack] = arrangement[src_stack][0:-num_of_crates_to_move]

        dst_stack = move[INDEX_STACK_DST] - 1

        # maintain order - add items in the order they were removed
        if (maintain_order):
            arrangement[dst_stack].extend(crate_holding)

        else:
            # remove items LIFO, add items FILO
            for i in range(0, num_of_crates_to_move):
                current_crate = crate_holding.pop()
                arrangement[dst_stack].extend(current_crate)

        # reset variables
        crate_holding = []

    return arrangement

def get_topmost_crates(arrangement):

    topmost_string = ''

    for stack in arrangement:
        topmost_string = topmost_string + str(stack[-1:].pop())

    return topmost_string

def simulate_arrangement(raw_input_starting_arrangement, raw_input_moves, maintain_order):
    starting_arrangement = create_arrangement_dict(raw_input_starting_arrangement)

    moves = create_move_dict(raw_input_moves)

    return simulate_result(starting_arrangement, moves, maintain_order)

def main():
    # gather raw input
    raw_input_beginning_crates = []
    raw_input_moves = []
    begin_move_input = False

    # retrieve the path 
    path = os.path.join(os.getcwd(), INPUT_DIR, INPUT_FILE)

    # open file
    with open(path, 'r') as file:
        for line in file:
            if (line.strip() == ''):
                begin_move_input = True
                continue

            if (begin_move_input):
                raw_input_moves.append(line)
            else: 
                raw_input_beginning_crates.append(line)

    # Simulate move arrangement if order is not maintained (crane only pick up one item at once)
    resulting_arrangement = simulate_arrangement(raw_input_beginning_crates, raw_input_moves, False)
    print(get_topmost_crates(resulting_arrangement))

    # Simulate move arrangement if order is maintained (crane can pick up multiple items at once)
    resulting_arrangement = simulate_arrangement(raw_input_beginning_crates, raw_input_moves, True)
    print(get_topmost_crates(resulting_arrangement))

if __name__ == '__main__':
    main()

