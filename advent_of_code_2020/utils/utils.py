import re
import numpy as np


def read_list_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines

def read_password_file(input_file):
    lines = read_list_file(input_file)
    passwords_policies = [parse_password_policy(line) for line in lines]
    return passwords_policies

def parse_password_policy(line):
    match = re.search("(\d*)\-(\d*)\s(\w):\s(\w*)", line)
    policy = ([int(match.group(1)), int(match.group(2))], match.group(3))
    password = match.group(4)
    return password, policy

# The main function to sort an array of given size
def sort_list(arr, kind='quicksort'):
    return np.sort(arr, kind=kind).tolist()

def find_pair_match(arr, target):
    arr = sort_list(arr)
    num_elements = len(arr)

    for num in arr[:(num_elements // 2)]:
        match_target = target - num
        for other_num in arr[::-1]:
            if other_num < match_target:
                break
            elif other_num == match_target:
                return (num, other_num)

    return (None, None)


def find_triplet_match(arr, target):
    arr = sort_list(arr)
    num_elements = len(arr)

    for i, first_num in enumerate(arr):
        top_index = num_elements
        for second_num in arr[(i + 1):]:
            match_target = target - first_num - second_num

            if match_target < 0:
                break

            for last_num in arr[top_index::-1]:
                if last_num < match_target:
                    break
                elif last_num == match_target:
                    return (first_num, second_num, last_num)
                top_index -= 1

    return (None, None, None)


def find_pair_match_2020(arr):
    return find_pair_match(arr, 2020)


def find_triplet_match_2020(arr):
    return find_triplet_match(arr, 2020)


def does_password_meet_policy_count(password, policy):
    num_occurance_range, target = policy

    count_occurances = 0
    for c in password:
        if c == target:
            count_occurances += 1

    if count_occurances >= num_occurance_range[0] and count_occurances <= num_occurance_range[1]:
        return True
    else:
        return False

def does_password_meet_policy_position(password, policy):
    occurance_positions, target = policy

    count_occurances = 0
    if password[occurance_positions[0] - 1] == target:
        count_occurances += 1
    if password[occurance_positions[1] - 1] == target:
        count_occurances += 1

    if count_occurances == 1:
        return True
    else:
        return False
