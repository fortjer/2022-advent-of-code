# day6.py

# --- IMPORTS ---
import os
import sys

# --- CONSTANTS ---
INPUT_FILE = 'day6-input.txt'
INPUT_DIR = 'input/'

def is_sequence_found(curr_sequence_to_check):
    letter_dict = dict()

    for letter in curr_sequence_to_check:
        if letter_dict.get(letter):
            letter_dict[letter] = int(letter_dict[letter]) + 1
        else:
            letter_dict.update({letter: int(1)})

    for key in letter_dict:
        if int(letter_dict[key]) > 1:
            return False

    return True

def find_start_of_packet(input_string, sequence_length):
    end_range_length = len(input_string) - sequence_length + 1

    for current_index in range(0, end_range_length):
        start_split_index = 0 + current_index
        end_split_index = sequence_length + current_index
        curr_sequence_to_check = input_string[start_split_index:end_split_index]
        
        if is_sequence_found(curr_sequence_to_check):
            break

    print(curr_sequence_to_check)

    return (current_index + sequence_length)

def main():
    input = []

    # Retrieve path containing input file
    path = os.path.join(os.getcwd(), INPUT_DIR, INPUT_FILE)

    with open(path, 'r') as file:
        for line in file:
            input.append(line.strip())

    starting_character_index = find_start_of_packet(input[0], 4)
    print(starting_character_index)

    starting_message_index = find_start_of_packet(input[0], 14)
    print(starting_message_index)

if __name__ == '__main__':
    main()