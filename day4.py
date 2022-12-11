# day4.py

# -- IMPORTS --
import os
import sys

# -- CONSTANTS --
INPUT_DIR = '/input/'
INPUT_FILE = 'day4-input.txt'

def clean_string_input_to_int(elf_pairs, pair_num):
    assignment = elf_pairs[pair_num - 1].split('-')
    assignment[0] = int(assignment[0])
    assignment[1] = int(assignment[1])

    return assignment

def create_dict_entry(line):
    line = line.strip()

    elf_pairs = line.split(',')

    first_elf_assignment = clean_string_input_to_int(elf_pairs, 1)
    second_elf_assignment = clean_string_input_to_int(elf_pairs, 2)

    pair = (first_elf_assignment, second_elf_assignment)
    
    return pair

def num_of_pairs_with_overlap_assignments(dict):
    overlaps = 0
    overlap_found = False

    for entry in dict:
        first_elf = entry[0]
        second_elf = entry[1]

        first_elf_begin_bound = first_elf[0]
        first_elf_end_bound = first_elf[1]
        second_elf_begin_bound = second_elf[0]
        second_elf_end_bound = second_elf[1]

        if (first_elf_begin_bound >= second_elf_begin_bound):
            if (first_elf_begin_bound <= second_elf_end_bound):
                overlap_found = True 

        if (first_elf_end_bound >= second_elf_begin_bound):
            if (first_elf_end_bound <= second_elf_end_bound):
                overlap_found = True        

        if (second_elf_begin_bound >= first_elf_begin_bound):
            if (second_elf_begin_bound <= first_elf_end_bound):
                overlap_found = True 

        if (second_elf_end_bound >= first_elf_begin_bound):
            if (second_elf_end_bound <= first_elf_end_bound):
                overlap_found = True    

        if overlap_found:
            
            overlaps = overlaps + 1

        overlap_found = False

    return overlaps

def num_of_pairs_with_contained_assignments(dict):
    containments = 0
    containment_found = False

    for entry in dict:
        first_elf = entry[0]
        second_elf = entry[1]

        first_elf_begin_bound = first_elf[0]
        first_elf_end_bound = first_elf[1]
        second_elf_begin_bound = second_elf[0]
        second_elf_end_bound = second_elf[1]

        if (first_elf_begin_bound <= second_elf_begin_bound):
            if (first_elf_end_bound >= second_elf_end_bound):
                containment_found = True 

        if (second_elf_begin_bound <= first_elf_begin_bound):
            if (second_elf_end_bound >= first_elf_end_bound):
                containment_found = True

        if containment_found:
            containments = containments + 1

        containment_found = False

    return containments

def main():
    # Retrive the path containing the input file 
    path = os.path.join(os.getcwd() + INPUT_DIR + INPUT_FILE)

    dict = []

    with open(path, 'r') as file:
        for line in file:
            dict_entry = create_dict_entry(line)
            dict.append(dict_entry)

    print(num_of_pairs_with_contained_assignments(dict))
    print(num_of_pairs_with_overlap_assignments(dict))

if __name__ == '__main__':
    main()