# day7.py

# -- IMPORTS --
import os
import sys

# -- CONSTANTS --
INPUT_FILE = 'day7-input.txt'
INPUT_DIR = 'input/'

USER_COMMAND = '$'
CHG_DIR_COMMAND = 'cd'
LIST_COMMAND = 'ls'
MOVE_OUT_DIR = '..'
ROOT_DIR = '/'
ITEM_DIRECTORY = 'dir'

def retrieve_size(dir_sizes, subdirs, curr_dir):

    if curr_dir in subdirs:
        subdirs_in_curr_dir = subdirs[curr_dir]

        for curr_subdir in subdirs_in_curr_dir:

            path_curr_subdir = curr_dir + curr_subdir + '/'    

            dir_sizes[curr_dir] = dir_sizes[curr_dir] + retrieve_size(dir_sizes, subdirs, path_curr_subdir)

    return dir_sizes[curr_dir]

def readjust_size_for_subdirs(dir_sizes, subdirs, curr_dir):
    path_curr_subdir = None

    if curr_dir in subdirs:
        subdirs_in_curr_dir = subdirs[curr_dir]

        for curr_subdir in subdirs_in_curr_dir:

            path_curr_subdir = curr_dir + curr_subdir + '/'

            dir_sizes[curr_dir] = dir_sizes[curr_dir] + retrieve_size(dir_sizes, subdirs, path_curr_subdir)

    return dir_sizes

def find_dir_sizes(dir_structure):
    dir_sizes = {}
    subdirs = {}
    current_dir = ''
    running_total = 0
    subdir_list = []

    # iterate through all entries in the directory structure
    for entry in dir_structure:

        # if we are looking at a different direcctory
        if current_dir != entry[0]:

            # If this is not the first iteration
            # Then we need to record the running total of the last iteration
            # And add it as an entry in the dir_sizes dictionary
            if not current_dir == '':
                dir_sizes[current_dir] = running_total

            # reset values
            current_dir = entry[0]
            running_total = 0
            subdir_list = []

        # Check if entry is a subdirectory
        if entry[1] == 'dir':

            # Check if entry already exists in the subdirectory list
            # If it does - retrieve the current list
            if current_dir in subdirs:
                subdirs[current_dir] = subdirs[current_dir].append(entry[2])

            # Otherwise - just add it to the new lsit
            else:
                # add new subdirectory to list
                subdir_list.append(entry[2])

            # assign new subdirectory list to subdir dictionary
            subdirs[current_dir] = subdir_list
        
        # increment running total
        running_total = running_total + int(entry[3])

    # check the last iteration
    if not current_dir in dir_sizes:
        dir_sizes[current_dir] = running_total

    # check for subdirectories and their sizes 
    # i.e. - readjust the totals for directories within other directories
    if subdirs:
        dir_sizes = readjust_size_for_subdirs(dir_sizes, subdirs, ROOT_DIR)

    return dir_sizes

def create_dir_path(curr_dir_list):
    curr_path = ''

    for item in curr_dir_list:
        curr_path = curr_path + item 

        if item == ROOT_DIR:
            continue
        else:
            curr_path = curr_path + '/'

    return curr_path

def parse_input(input_dict):
    list_mode = False
    dir_structure = []
    curr_dir = []

    # iterate through input dictionary
    for line in input_dict:

        # Check if user command 
        if line[0] == USER_COMMAND:
            
            list_mode = False
            
            # Check if change directory command
            if line[1] == CHG_DIR_COMMAND:

                if line[2] == ROOT_DIR:
                    curr_dir = [line[2]]

                elif line[2] == MOVE_OUT_DIR:
                    curr_dir.pop()

                else:
                    curr_dir.append(line[2])

            # Check if list command:
            if line[1] == LIST_COMMAND:

                list_mode = True
                continue

        # Check if in list mode
        if list_mode:
            
            dir_path = create_dir_path(curr_dir[0:len(curr_dir)])

            # Check if item is a dir
            if line[0] == ITEM_DIRECTORY:
                curr_item = [dir_path, 'dir', line[1], 0]
                dir_structure.append(curr_item)
            
            # Else - item is a file
            else:
                curr_item = [dir_path, 'fil', line[1], line[0]]
                dir_structure.append(curr_item)

    return dir_structure

def filter_dir_sizes(dir_sizes, max_size_limit):
    new_dir_sizes = {}

    for entry in dir_sizes:

        if dir_sizes[entry] < max_size_limit:
            new_dir_sizes[entry] = dir_sizes[entry]
    
    return new_dir_sizes

def sum_dir_sizes(dir_sizes):
    running_total = 0

    for entry in dir_sizes:
        running_total = running_total + dir_sizes[entry]

    return running_total

def perform_tests(file_contents):
    # gather all directories
    all_dirs = []

    for line in file_contents:
        if (line[0] == 'dir'):
            all_dirs.append(line[1])
        
        if not (line[0] == '$'):
            continue 

        if not (line[1] == 'cd'):
            continue

        if (line[2] == '..'):
            continue 

        if line[2] in all_dirs:
            continue 

        all_dirs.append(line[2])

def determine_directory_to_delete(total_avail_disk_space, needed_disk_space, dir_sizes):
    root_dir_size = None
    directory_to_delete = None
    size_of_directory_to_delete = None
    tolerance = None

    if dir_sizes[ROOT_DIR]:
        root_dir_size = dir_sizes[ROOT_DIR]

    free_disk_space = total_avail_disk_space - root_dir_size

    target_disk_spaced_needed = needed_disk_space - free_disk_space

    # Set default tolerance
    tolerance = 0 - total_avail_disk_space

    if dir_sizes:
        for dir in dir_sizes:

            size_still_needed = target_disk_spaced_needed - dir_sizes[dir]

            # If the directory is too small, continue looking
            if (size_still_needed > 0):
                continue 

            # If the directory is large enough
            # BUT smaller than the previously selected directory to delete,
            # We are choosing the currently selected directory for deletion
            if (size_still_needed > tolerance):
                directory_to_delete = dir
                size_of_directory_to_delete = dir_sizes[dir]
                tolerance = size_still_needed

    print("Directory to delete: " + str(directory_to_delete))

    return size_of_directory_to_delete
        

def main():
    file_contents = []
    dir_sizes = None

    # Build path to input file
    path = os.path.join(os.getcwd(), INPUT_DIR, INPUT_FILE)

    # Open and read through input file
    with open(path, 'r') as file:
        for line in file:
            current_line = line.strip().split(' ')
            file_contents.append(current_line)

    # perform_tests(file_contents)

    file_contents = parse_input(file_contents)

    # iterate through parsed input to find dirs and their sizes
    dir_sizes = find_dir_sizes(file_contents)

    # filter based on directories with a max size limit
    filtered_dir_sizes = filter_dir_sizes(dir_sizes, 100000)

    # return total sum of all filtered dir sizes
    print("Sum of directory sizes with total size of at most 100k: " + str(sum_dir_sizes(filtered_dir_sizes)))

    # choose which directory to delete based on 
    # total disk space, allocated space, and needed space
    print("Smallest directory we can delete to allocate space takes up: " + str(determine_directory_to_delete(70000000, 30000000, dir_sizes)))

if __name__ == '__main__':
    main()