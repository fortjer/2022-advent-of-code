# day3.py

# --- IMPORTS ---
import os
import sys 

# --- CONSTANTS ---
INPUT_DIR = 'input/'
INPUT_FILE = 'day3-input.txt'

PRIORITY_STRING_CHECK = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calculate_priority(char):
    return (PRIORITY_STRING_CHECK.index(char) + 1)

def calculate_item_type_priority(input_path):
    first_compartment = ''
    second_compartment = ''
    current_priority = 0
    mid_index = -1
    same_items = ''

    input_file = open(input_path, 'r')

    for line in input_file:
        mid_index = ((len(line) - 1) / 2)
        mid_index = int(mid_index)

        first_compartment = line[0:mid_index].strip()
        second_compartment = line[mid_index:].strip()

        for letter in second_compartment:
            # If the letter was already seen and accounted for continue
            if letter in same_items:
                continue
            if letter in first_compartment:
                current_priority = current_priority + calculate_priority(letter)
                same_items = same_items + letter

        # Reset variables
        same_items = ''

    return current_priority


def calculate_badge_priority(input_path):
    total_iterations = 0
    first_rucksack = ''
    second_rucksack = ''
    third_rucksack = ''
    current_priority = 0
    mid_index = -1
    same_items = ''

    with open(input_path, 'r') as input_file:
        lines = input_file.readlines()

    total_iterations = int(len(lines) / 3)

    for i in range(0, total_iterations):
        first_rucksack = lines[(3 * i)].strip()
        second_rucksack = lines[(3 * i) + 1].strip()
        third_rucksack = lines[(3 * i) + 2].strip()

        for letter in second_rucksack:
            # If the letter was already seen and accounted for, continue
            if letter in same_items:
                continue
            if letter in first_rucksack:
                same_items = same_items + letter 

        # Reset variables
        first_rucksack = same_items
        same_items = ''

        for letter in third_rucksack:
            if letter in same_items:
                continue
            if letter in first_rucksack:
                current_priority = current_priority + calculate_priority(letter)
                same_items = same_items + letter 

        # Reset variables
        same_items = ''

    return current_priority

def main():
  
    # Create path
    input_path = os.path.join(os.getcwd(), INPUT_DIR, INPUT_FILE)

    print(calculate_item_type_priority(input_path))

    print(calculate_badge_priority(input_path))

if __name__ == "__main__":
    main()