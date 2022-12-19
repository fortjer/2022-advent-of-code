# day9.py

# -- IMPORTS --
import os

# -- CONSTANTS --
INPUT_DIR = 'input/'
INPUT_FILE = 'day9-input.txt'

INDEX_DIRECTION = 0
INDEX_NUM_OF_SPACES = 1

INDEX_X_COORD = 0
INDEX_Y_COORD = 1

DIRECTION_LEFT = 'L'
DIRECTION_RIGHT = 'R'
DIRECTION_UP = 'U'
DIRECTION_DOWN = 'D'

def simulate_2D_bridge(move_list):
    prior_tail_coords = []
    curr_coord_head = (0, 0)
    curr_coord_tail = (0, 0)
    diagonal_triggered = False
    overlap_triggered = False

    for entry in move_list:
        move = entry.split(" ")

        if move[INDEX_DIRECTION] == DIRECTION_RIGHT:

            # move the head
            curr_coord_head = (curr_coord_head[INDEX_X_COORD] + int(move[INDEX_NUM_OF_SPACES]), curr_coord_head[INDEX_Y_COORD])

            # track tail movement
            for curr_num_of_spaces in range(1, int(move[INDEX_NUM_OF_SPACES]) + 1):

                # add the current position to the tracked tail coordinates
                # if the coords were not tracked previously
                if curr_coord_tail not in prior_tail_coords:
                    if not diagonal_triggered or not overlap_triggered:
                        prior_tail_coords.append((curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD]))

                # if the tail is on a seperate y-plane than the head
                # the first move is a diagonal - which is okay (which means the tail does not move anywhere this turn)
                if not diagonal_triggered:
                    if not curr_coord_tail[INDEX_Y_COORD] == curr_coord_head[INDEX_Y_COORD]:
                        diagonal_triggered = True
                        continue 

                # if at the beginning of head's movement, the head was on top of the tail
                # the tail does not move anywhere this turn
                if not overlap_triggered:
                    if curr_coord_head[INDEX_Y_COORD] == curr_coord_tail[INDEX_Y_COORD]:
                        if (abs(curr_coord_head[INDEX_X_COORD]) - int(move[INDEX_NUM_OF_SPACES])) == curr_coord_tail[INDEX_X_COORD]:
                            overlap_triggered = True
                            continue 

                # Otherwise, let's move the tail in that direction
                if diagonal_triggered:

                    # Check if not taught enough to pull out of the diagonal 
                    if curr_coord_tail[INDEX_X_COORD] >= (curr_coord_head[INDEX_X_COORD] - int(move[INDEX_NUM_OF_SPACES]) + curr_num_of_spaces - 1):
                        continue

                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD] + 1, curr_coord_head[INDEX_Y_COORD])
                    diagonal_triggered = False 
                
                elif overlap_triggered:
                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD] + 1, curr_coord_tail[INDEX_Y_COORD])
                    overlap_triggered = False
                
                else:
                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD] + 1, curr_coord_tail[INDEX_Y_COORD])

        elif move[INDEX_DIRECTION] == DIRECTION_LEFT:

            # move the head
            curr_coord_head = (curr_coord_head[INDEX_X_COORD] - int(move[INDEX_NUM_OF_SPACES]), curr_coord_head[INDEX_Y_COORD])

            # track tail movement
            for curr_num_of_spaces in range(1, int(move[INDEX_NUM_OF_SPACES]) + 1):

                # add the current position to the tracked tail coordinates
                # if the coords were not tracked previously
                if curr_coord_tail not in prior_tail_coords:
                    if not diagonal_triggered or not overlap_triggered:
                        prior_tail_coords.append((curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD]))

                # if the tail is on a seperate y-plane than the head
                # the first move is a diagonal - which is okay (which means the tail does not move anywhere this turn)
                if not diagonal_triggered:
                    if not curr_coord_tail[INDEX_Y_COORD] == curr_coord_head[INDEX_Y_COORD]:
                        diagonal_triggered = True
                        continue 

                # if at the beginning of head's movement, the head was on top of the tail
                # the tail does not move anywhere this turn
                if not overlap_triggered:
                    if curr_coord_head[INDEX_Y_COORD] == curr_coord_tail[INDEX_Y_COORD]:
                        if (abs(curr_coord_head[INDEX_X_COORD]) - int(move[INDEX_NUM_OF_SPACES])) == curr_coord_tail[INDEX_X_COORD]:
                            overlap_triggered = True
                            continue 

                # Otherwise, let's move the tail in that direction
                if diagonal_triggered:
                    # Check if not taught enough to pull out of the diagonal 
                    if (curr_coord_tail[INDEX_X_COORD]) <= (curr_coord_head[INDEX_X_COORD] + int(move[INDEX_NUM_OF_SPACES]) - curr_num_of_spaces + 1):
                        continue

                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD] - 1, curr_coord_head[INDEX_Y_COORD])
                    diagonal_triggered = False 

                elif overlap_triggered:
                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD] - 1, curr_coord_tail[INDEX_Y_COORD])
                    overlap_triggered = False
                
                else:
                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD] - 1, curr_coord_tail[INDEX_Y_COORD])

        elif move[INDEX_DIRECTION] == DIRECTION_UP:

            # move the head
            curr_coord_head = (curr_coord_head[INDEX_X_COORD],  curr_coord_head[INDEX_Y_COORD] + int(move[INDEX_NUM_OF_SPACES]))

            # track tail movement
            for curr_num_of_spaces in range(1, int(move[INDEX_NUM_OF_SPACES]) + 1):

                # add the current position to the tracked tail coordinates
                # if the coords were not tracked previously
                if curr_coord_tail not in prior_tail_coords:
                    if not diagonal_triggered or not overlap_triggered:
                        prior_tail_coords.append((curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD]))

                # if the tail is on a seperate y-plane than the head
                # the first move is a diagonal - which is okay (which means the tail does not move anywhere this turn)
                if not diagonal_triggered:
                    if not curr_coord_tail[INDEX_X_COORD] == curr_coord_head[INDEX_X_COORD]:
                        diagonal_triggered = True
                        continue 

                # if at the beginning of head's movement, the head was on top of the tail
                # the tail does not move anywhere this turn
                if not overlap_triggered:
                    if curr_coord_head[INDEX_X_COORD] == curr_coord_tail[INDEX_X_COORD]:
                        if (abs(curr_coord_head[INDEX_Y_COORD]) - int(move[INDEX_NUM_OF_SPACES])) == curr_coord_tail[INDEX_Y_COORD]:
                            overlap_triggered = True
                            continue 

                # Otherwise, let's move the tail in that direction
                if diagonal_triggered:

                    # Check if not taught enough to pull out of the diagonal 
                    if curr_coord_tail[INDEX_Y_COORD] >= (curr_coord_head[INDEX_Y_COORD] - int(move[INDEX_NUM_OF_SPACES]) + curr_num_of_spaces - 1):
                        continue

                    curr_coord_tail = (curr_coord_head[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD] + 1)
                    diagonal_triggered = False 
                
                elif overlap_triggered:
                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD] + 1)
                    overlap_triggered = False
                
                else:
                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD] + 1)

        elif move[INDEX_DIRECTION] == DIRECTION_DOWN:

            # move the head
            curr_coord_head = (curr_coord_head[INDEX_X_COORD],  curr_coord_head[INDEX_Y_COORD] - int(move[INDEX_NUM_OF_SPACES]))

            # track tail movement
            for curr_num_of_spaces in range(1, int(move[INDEX_NUM_OF_SPACES]) + 1):

                # add the current position to the tracked tail coordinates
                # if the coords were not tracked previously
                if curr_coord_tail not in prior_tail_coords:
                    if not diagonal_triggered or not overlap_triggered:
                        prior_tail_coords.append((curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD]))

                # if the tail is on a seperate y-plane than the head
                # the first move is a diagonal - which is okay (which means the tail does not move anywhere this turn)
                if not diagonal_triggered:
                    if not curr_coord_tail[INDEX_X_COORD] == curr_coord_head[INDEX_X_COORD]:
                        diagonal_triggered = True
                        continue 

                # if at the beginning of head's movement, the head was on top of the tail
                # the tail does not move anywhere this turn
                if not overlap_triggered:
                    if curr_coord_head[INDEX_X_COORD] == curr_coord_tail[INDEX_X_COORD]:
                        if (abs(curr_coord_head[INDEX_Y_COORD]) - int(move[INDEX_NUM_OF_SPACES])) == curr_coord_tail[INDEX_Y_COORD]:
                            overlap_triggered = True
                            continue 

                # Otherwise, let's move the tail in that direction
                if diagonal_triggered:

                    # Check if not taught enough to pull out of the diagonal 
                    if (curr_coord_tail[INDEX_Y_COORD]) <= (curr_coord_head[INDEX_Y_COORD] + int(move[INDEX_NUM_OF_SPACES]) - curr_num_of_spaces + 1):
                        continue

                    curr_coord_tail = (curr_coord_head[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD] - 1)
                    diagonal_triggered = False 
                
                elif overlap_triggered:
                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD] - 1)
                    overlap_triggered = False
                
                else:
                    curr_coord_tail = (curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD] - 1)

        # Check final tail move
        if curr_coord_tail not in prior_tail_coords:
            if not diagonal_triggered or not overlap_triggered:
                prior_tail_coords.append((curr_coord_tail[INDEX_X_COORD], curr_coord_tail[INDEX_Y_COORD]))
        

        print("Head" + str(curr_coord_head))
        print("Tail" + str(curr_coord_tail))

    return(prior_tail_coords)
    
def visualize_2D_bridge(tail_coords):
    max_x_coord = 0
    max_y_coord = 0
    visualization = []
    curr_row = []

    for entry in tail_coords:
        if entry[INDEX_X_COORD] > max_x_coord:
            max_x_coord = entry[INDEX_X_COORD]

        if entry[INDEX_Y_COORD] > max_y_coord:
            max_y_coord = entry[INDEX_Y_COORD]

    for y_coord in range(0, max_y_coord + 2):
        for x_coord in range(0, max_x_coord + 2):
            curr_coords = (x_coord, y_coord)

            if curr_coords in tail_coords:
                curr_row.append('#')
            else:
                curr_row.append('.')

        visualization.append(curr_row)
        curr_row = []

    return visualization

def print_visualization(visualization):
    curr_line = ''

    for line in reversed(visualization):
        for entry in line:
            curr_line = curr_line + entry
        
        print(curr_line)
        curr_line = ''

def main():

    file_contents = []

    # Generate path to input file
    path = os.path.join(os.getcwd(), INPUT_DIR, INPUT_FILE)

    # Read through file contents
    with open(path, 'r') as file:
        for line in file:
            file_contents.append(line.strip())

    # Retrieve tracked tail coordinates
    prior_tail_coords = simulate_2D_bridge(file_contents)

    # Calculate number of positions tail visited at least once
    print(len(prior_tail_coords))

    # Print visual of the 2D bridge
    #visualization = visualize_2D_bridge(prior_tail_coords)

    #print_visualization(visualization)

if __name__ == '__main__':
    main()