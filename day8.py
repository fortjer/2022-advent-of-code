# day8.py

# -- IMPORTS --
import os
 
# -- CONSTANTS --
INPUT_FILE = 'day8-test1.txt'
INPUT_DIR = 'input/'

INDEX_GRID_VALUE = 0
INDEX_GRID_TOWARDS_NORTH_VISIBILITY = 0
INDEX_GRID_TOWARDS_SOUTH_VISIBILITY = 1
INDEX_GRID_TOWARDS_WEST_VISIBILITY = 2
INDEX_GRID_TOWARDS_EAST_VISIBILITY = 3

INDEX_COORD_ROW = 0
INDEX_COORD_COL = 1

RESULT_NOT_EVAL = -1
RESULT_NOT_VISIBLE = 0
RESULT_VISIBLE = 1

def generate_2D_value_grid(file_contents):
    grid = {}

    # Each line in the file is a row
    for x, line in enumerate(file_contents, start=1):

        # Each character in a line is the column:
        for y, character in enumerate(line, start=1):

            coords = (x, y)
            grid[coords] = character

    return grid

def generate_2D_tree_visbility_grid(file_contents):
    grid = {}

    # Each line in the file is a row
    for x, line in enumerate(file_contents, start=1):

        # Each character in a line is the column:
        for y, character in enumerate(line, start=1):

            coords = (x, y)
            grid[coords] = [RESULT_NOT_EVAL, RESULT_NOT_EVAL, RESULT_NOT_EVAL, RESULT_NOT_EVAL]

    return grid

def get_total_rows(file_contents):
    line_number = 0

    for line in file_contents:
        line_number = line_number + 1

    return line_number

def get_total_cols(file_contents):
    char_number = 0

    for line in file_contents:
        char_number = len(line)
        break 

    return char_number

def calculate_visibility(value_grid, coords, visibility):
    # Calculate Northern visibility, if not evaluated
    if visibility[INDEX_GRID_TOWARDS_NORTH_VISIBILITY] == RESULT_NOT_EVAL:
        is_tree_visible = True
        curr_value = int(value_grid[coords])

        for x_coord in reversed(range(1, coords[INDEX_COORD_ROW])):
            comparison_coords = (x_coord, int(coords[INDEX_COORD_COL]))
            if curr_value <= int(value_grid[comparison_coords]):
                is_tree_visible = False

        if is_tree_visible:
            visibility[INDEX_GRID_TOWARDS_NORTH_VISIBILITY] = RESULT_VISIBLE
        else:
            visibility[INDEX_GRID_TOWARDS_NORTH_VISIBILITY] = RESULT_NOT_VISIBLE

    return visibility

def determine_visibility(value_grid, visibility_grid, total_rows, total_cols):
    for entry in visibility_grid:

        # Check if entry is on the Northern edge:
        if entry[INDEX_COORD_ROW] == 1:
            visibility = visibility_grid[entry]
            visibility[INDEX_GRID_TOWARDS_NORTH_VISIBILITY] = RESULT_VISIBLE
            visibility_grid[entry] = visibility

        # Check if entry is on the Southern edge:
        elif entry[INDEX_COORD_ROW] == total_rows:
            visibility = visibility_grid[entry]
            visibility[INDEX_GRID_TOWARDS_SOUTH_VISIBILITY] = RESULT_VISIBLE
            visibility_grid[entry] = visibility

        # Check if entry is on the Western edge:
        if entry[INDEX_COORD_COL] == 1:
            visibility = visibility_grid[entry]
            visibility[INDEX_GRID_TOWARDS_WEST_VISIBILITY] = RESULT_VISIBLE
            visibility_grid[entry] = visibility

        # Check if entry is on the Eastern edge:
        elif entry[INDEX_COORD_COL] == total_cols:
            visibility = visibility_grid[entry]
            visibility[INDEX_GRID_TOWARDS_EAST_VISIBILITY] = RESULT_VISIBLE
            visibility_grid[entry] = visibility

        # Calculate remaining visibility:
        visibility_grid[entry] = calculate_visibility(value_grid, entry, visibility_grid[entry])

    return visibility_grid



def main():
    file_contents = []

    # Generate path to retrieve input file
    path = os.path.join(os.getcwd(), INPUT_DIR, INPUT_FILE)

    # Iterate through input file
    with open(path, 'r') as file:
        for line in file:
            file_contents.append(line.strip())

    total_rows = get_total_rows(file_contents)

    total_cols = get_total_cols(file_contents)

    # Generate a 2D value grid based on the file contents
    value_grid = generate_2D_value_grid(file_contents)

    # Generate a 2D tree visibility grid based on the file contents
    visiblity_grid = generate_2D_tree_visbility_grid(file_contents)

    # Score and determine visibility of trees from the outer perimeter
    visiblity_grid = determine_visibility(value_grid, visiblity_grid, total_rows, total_cols)

    print(visiblity_grid)

if __name__ == '__main__':
    main()