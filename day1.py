# day1.py

# --- IMPORTS ---
import os
import math
import sys

# --- CONSTANTS --- 
INPUT_DIR = 'input/'
INPUT_FILE = 'day1-input.txt'

def merge(left_list, right_list):
    merged_list = []
    left_curr_index = 0
    right_curr_index = 0

    if len(left_list):
        length_left_list = len(left_list)
    else:
        length_left_list = 0

    if len(right_list):
        length_right_list = len(right_list)
    else:
        length_right_list = 0

    while (left_curr_index < length_left_list) and (right_curr_index < length_right_list):
        if (left_list[left_curr_index] >= right_list[right_curr_index]):
            merged_list.append(left_list[left_curr_index])
            left_curr_index = left_curr_index + 1
        else:
            merged_list.append(right_list[right_curr_index])
            right_curr_index = right_curr_index + 1

    while (left_curr_index < length_left_list):
        merged_list.append(left_list[left_curr_index])
        left_curr_index = left_curr_index + 1

    while (right_curr_index < length_right_list):
        merged_list.append(right_list[right_curr_index])
        right_curr_index = right_curr_index + 1   

    return merged_list

def merge_sort(list, begin_index, end_index):
    if (end_index - begin_index < 1):
        return list
    
    mid_index = math.floor((end_index - begin_index) / 2) + begin_index

    left_list = merge_sort(list[(begin_index - begin_index):(mid_index - begin_index + 1)], begin_index, mid_index)

    right_list = merge_sort(list[(mid_index - begin_index + 1):(end_index - begin_index + 1)], mid_index + 1, end_index)

    merged_list = merge(left_list, right_list)

    return merged_list

def order_list_desc(list):
    list = merge_sort(list, 0, len(list) - 1)

    return list

def find_elf_with_largest_calories(list):
    curr_largest_elf_index = -1
    curr_largest_calories = -1
    
    for elf_index in range(0, len(list) - 1): 
        if list[elf_index] > curr_largest_calories:
            curr_largest_elf_index = elf_index
            curr_largest_calories = list[elf_index]

    if curr_largest_elf_index < 0:
        sys.exit('Error: No largest elf found.')
    
    return curr_largest_elf_index

def sum_list(list):
    running_tally = 0
    
    for value in list:
        running_tally = running_tally + value

    return running_tally 

def main():
    # Initial variables
    elf_list = []
    curr_elf_calories = 0
    
    # Create input file path
    path = os.path.join(os.getcwd(), INPUT_DIR, INPUT_FILE)

    # Open the input file
    input_file = open(path, "r")

    # Iterate through file, noting each Elf and the number of Calories they are carrying
    for line in input_file:
        
        # Check if empty line - indicates that it is the end of the inventory for the current Elf
        # If line has characters after stripping - add that as calories to their inventory
        # Else line is empty - starting tracking the next Elf
        if line.strip():
            curr_elf_calories = curr_elf_calories + int(line)
        
        else: 
            # Add Elf to the Elf Dictionary
            elf_list.append(curr_elf_calories)

            # Reset values
            curr_elf_calories = 0

    # Sort elf dictionary by number of calories held - from largest to smallest
    answer_elf_index = find_elf_with_largest_calories(elf_list)
    
    # Display answer
    print(elf_list[answer_elf_index])

    # Generate ordered list
    ordered_elf_list = order_list_desc(elf_list)

    # Retrieve top three Elves and sum up the total calories 
    print(sum_list(ordered_elf_list[:3]))

if __name__ == "__main__":
    main()