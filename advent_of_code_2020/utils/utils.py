import logging
import re
import numpy as np


logger = logging.getLogger(__name__)


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

def read_forest_file(input_file):
    lines = read_list_file(input_file)
    forest_base = [[1 if c == "#" else 0 for c in line.rstrip()] for line in lines]
    return forest_base

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

def count_trees_toboggan(forest_base, policy):
    num_rows = len(forest_base)
    num_columns = len(forest_base[0])

    vertical_position = 0
    horizontal_position = 0
    count_trees = 0

    while vertical_position < num_rows:
        if forest_base[vertical_position][horizontal_position % num_columns]:
            count_trees += 1
        vertical_position += policy[0]
        horizontal_position += policy[1]

    return count_trees


def day1(input_file):
    expenses = [int(expense) for expense in read_list_file(input_file)]
    match_pair = find_pair_match_2020(expenses)
    match_pair_multiple = match_pair[0] * match_pair[1]
    logger.info(f"The matching pair is {match_pair}, which is {match_pair_multiple} when multiplied")

    match_triplet = find_triplet_match_2020(expenses)
    match_triple_multiple = match_triplet[0] * match_triplet[1] * match_triplet[2]
    logger.info(f"The matching triplet is {match_triplet}, which is {match_triple_multiple} when multiplied")

def day2(input_file):
       passwords_policies = read_password_file(input_file)
       count_passwords_meet_policies = sum([
           # does_password_meet_policy_count(password, policy)
           does_password_meet_policy_position(password, policy)
           for password, policy in passwords_policies
       ])
       logger.info(f"{count_passwords_meet_policies} passwords meet their policy")

def day3(input_file):
    forest_base = read_forest_file(input_file)
    policies = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1]
    ]
    counts_trees = []
    for policy in policies:
        count_trees = count_trees_toboggan(forest_base, policy)
        counts_trees.append(count_trees)
        logger.info(f"Your tobogggan hits {count_trees} trees")

    count_trees_multiple = np.prod(counts_trees)
    logger.info(f"Multiplied together you get {count_trees_multiple}")
