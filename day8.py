# day8.py

# -- IMPORTS --
import os
 
# -- CONSTANTS --
INPUT_FILE = 'day8-input.txt'
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

def generate_2D_tree_eval_grid(file_contents):
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

def calculate_visibility(value_grid, coords, visibility, total_rows, total_cols):
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

    # Calculate Southern visibility, if not evaluated
    if visibility[INDEX_GRID_TOWARDS_SOUTH_VISIBILITY] == RESULT_NOT_EVAL:
        is_tree_visible = True 
        curr_value = int(value_grid[coords])

        for x_coord in range(coords[INDEX_COORD_ROW] + 1, total_rows + 1):
            comparison_coords = (x_coord, int(coords[INDEX_COORD_COL]))
            if curr_value <= int(value_grid[comparison_coords]):
                is_tree_visible = False

        if is_tree_visible:
            visibility[INDEX_GRID_TOWARDS_SOUTH_VISIBILITY] = RESULT_VISIBLE
        else:
            visibility[INDEX_GRID_TOWARDS_SOUTH_VISIBILITY] = RESULT_NOT_VISIBLE

    # Calculate Western visibility, if not evaluated
    if visibility[INDEX_GRID_TOWARDS_WEST_VISIBILITY] == RESULT_NOT_EVAL:
        is_tree_visible = True 
        curr_value = int(value_grid[coords])

        for y_coord in reversed(range(1, coords[INDEX_COORD_COL])):
            comparison_coords = (int(coords[INDEX_COORD_ROW]), y_coord)
            if curr_value <= int(value_grid[comparison_coords]):
                is_tree_visible = False 

        if is_tree_visible:
            visibility[INDEX_GRID_TOWARDS_WEST_VISIBILITY] = RESULT_VISIBLE
        else:
            visibility[INDEX_GRID_TOWARDS_WEST_VISIBILITY] = RESULT_NOT_VISIBLE

    # Calculate Eastern visibility, if not evaluted
    if visibility[INDEX_GRID_TOWARDS_EAST_VISIBILITY] == RESULT_NOT_EVAL:
        is_tree_visible = True
        curr_value = int(value_grid[coords])

        for y_coord in range(coords[INDEX_COORD_COL] + 1, total_cols + 1):
            comparison_coords = (int(coords[INDEX_COORD_ROW]), y_coord)
            if curr_value <= int(value_grid[comparison_coords]):
                is_tree_visible = False 

        if is_tree_visible:
            visibility[INDEX_GRID_TOWARDS_EAST_VISIBILITY] = RESULT_VISIBLE
        else:
            visibility[INDEX_GRID_TOWARDS_EAST_VISIBILITY] = RESULT_NOT_VISIBLE

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
        visibility_grid[entry] = calculate_visibility(value_grid, entry, visibility_grid[entry], total_rows, total_cols)

    return visibility_grid

def calculate_num_of_trees_visible(visibility_grid):
    num_of_trees_visible = 0

    for entry in visibility_grid:
        visibility = visibility_grid[entry]

        if RESULT_VISIBLE in visibility:
            num_of_trees_visible = num_of_trees_visible + 1

    return num_of_trees_visible

def calculate_scenic_score(value_grid, coords, scenic_score, total_rows, total_cols):

    # Calculate scenic score towards North if not evaluated
    if scenic_score[INDEX_GRID_TOWARDS_NORTH_VISIBILITY] == RESULT_NOT_EVAL:
        tentative_treehouse_height = int(value_grid[coords])
        curr_scenic_score = 0

        for x_coord in reversed(range(1, int(coords[INDEX_COORD_ROW]))):
            comparison_coords = (x_coord, int(coords[INDEX_COORD_COL]))

            comparison_tree_height = int(value_grid[comparison_coords])

            curr_scenic_score = curr_scenic_score + 1

            if tentative_treehouse_height <= comparison_tree_height:
                break

        scenic_score[INDEX_GRID_TOWARDS_NORTH_VISIBILITY] = curr_scenic_score

    # Calculate scenic score towards South if not evaluated
    if scenic_score[INDEX_GRID_TOWARDS_SOUTH_VISIBILITY] == RESULT_NOT_EVAL:
        tentative_treehouse_height = int(value_grid[coords])
        curr_scenic_score = 0

        for x_coord in range(int(coords[INDEX_COORD_ROW]) + 1, total_rows + 1):
            comparison_coords = (x_coord, int(coords[INDEX_COORD_COL]))

            comparison_tree_height = int(value_grid[comparison_coords])

            curr_scenic_score = curr_scenic_score + 1

            if tentative_treehouse_height <= comparison_tree_height:
                break

        scenic_score[INDEX_GRID_TOWARDS_SOUTH_VISIBILITY] = curr_scenic_score

    # Calculate scenice score towards West if not evaluated
    if scenic_score[INDEX_GRID_TOWARDS_WEST_VISIBILITY] == RESULT_NOT_EVAL:
        tentative_treehouse_height = int(value_grid[coords])
        curr_scenic_score = 0

        for y_coord in reversed(range(1, int(coords[INDEX_COORD_COL]))):
            comparison_coords = (int(coords[INDEX_COORD_ROW]), y_coord)

            comparison_tree_height = int(value_grid[comparison_coords])

            curr_scenic_score = curr_scenic_score + 1

            if tentative_treehouse_height <= comparison_tree_height:
                break

        scenic_score[INDEX_GRID_TOWARDS_WEST_VISIBILITY] = curr_scenic_score

    # Calculate scenic score towards East if not evaluated
    if scenic_score[INDEX_GRID_TOWARDS_EAST_VISIBILITY] == RESULT_NOT_EVAL:
        tentative_treehouse_height = int(value_grid[coords])
        curr_scenic_score = 0

        for y_coord in range(coords[INDEX_COORD_COL] + 1, total_cols + 1):
            comparison_coords = (int(coords[INDEX_COORD_ROW]), y_coord)

            comparison_tree_height = int(value_grid[comparison_coords])

            curr_scenic_score = curr_scenic_score + 1

            if tentative_treehouse_height <= comparison_tree_height:
                break

        scenic_score[INDEX_GRID_TOWARDS_EAST_VISIBILITY] = curr_scenic_score

    return scenic_score

def generate_2D_scenic_score_grid(value_grid, scenic_score_grid, total_rows, total_cols):
    for entry in scenic_score_grid:

        # Check if entry is on the Northern edge:
        if entry[INDEX_COORD_ROW] == 1:
            scenic_score = scenic_score_grid[entry]
            scenic_score[INDEX_GRID_TOWARDS_WEST_VISIBILITY] = 0
            scenic_score_grid[entry] = scenic_score

        # Check if entry is on the Southern edge
        if entry[INDEX_COORD_ROW] == total_rows:
            scenic_score = scenic_score_grid[entry]
            scenic_score[INDEX_GRID_TOWARDS_EAST_VISIBILITY] = 0
            scenic_score_grid[entry] = scenic_score

        # Check if entry is on the Western edge
        if entry[INDEX_COORD_COL] == 1:
            scenic_score = scenic_score_grid[entry]
            scenic_score[INDEX_GRID_TOWARDS_NORTH_VISIBILITY] = 0
            scenic_score_grid[entry] = scenic_score

        # Check if entry is on the Eastern edge
        if entry[INDEX_COORD_COL] == total_cols:
            scenic_score = scenic_score_grid[entry]
            scenic_score[INDEX_GRID_TOWARDS_SOUTH_VISIBILITY] = 0
            scenic_score_grid[entry] = scenic_score

        # Calculate remaining scenic score
        scenic_score_grid[entry] = calculate_scenic_score(value_grid, entry, scenic_score_grid[entry], total_rows, total_cols)

    return scenic_score_grid

def retrieve_highest_scenic_score(grid):
    highest_scenic_score = -1
    highest_entry = None

    for entry in grid:
        scenic_score = grid[entry]
        total_scenic_score = scenic_score[INDEX_GRID_TOWARDS_NORTH_VISIBILITY]
        total_scenic_score = total_scenic_score * scenic_score[INDEX_GRID_TOWARDS_SOUTH_VISIBILITY]
        total_scenic_score = total_scenic_score * scenic_score[INDEX_GRID_TOWARDS_WEST_VISIBILITY]
        total_scenic_score = total_scenic_score * scenic_score[INDEX_GRID_TOWARDS_EAST_VISIBILITY]

        if highest_scenic_score < total_scenic_score:
            highest_scenic_score = total_scenic_score
            highest_entry = entry

    print(grid)
    print(highest_entry)

    return highest_scenic_score

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
    visiblity_grid = generate_2D_tree_eval_grid(file_contents)

    # Score and determine visibility of trees from the outer perimeter
    visiblity_grid = determine_visibility(value_grid, visiblity_grid, total_rows, total_cols)

    # Calculate how many trees are visible from the outer perimeter
    print(calculate_num_of_trees_visible(visiblity_grid))

    # Generate initial scenic score grid
    scenic_store_grid = generate_2D_tree_eval_grid(file_contents)

    # Score and determine the "scenic score" for building a treehouse
    scenic_store_grid = generate_2D_scenic_score_grid(value_grid, scenic_store_grid, total_rows, total_cols)

    print(scenic_store_grid)

    # Retrieve highest scenic score
    print(retrieve_highest_scenic_score(scenic_store_grid))

if __name__ == '__main__':
    main()