import logging
import numpy as np


logger = logging.getLogger(__name__)


def read_list_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines

def read_int_list_file(input_file):
    lines = read_list_file(input_file)
    ints = [int(line.rstrip()) for line in lines]
    return ints

# The main function to sort an array of given size
def sort_list(arr, kind='quicksort'):
    return np.sort(arr, kind=kind).tolist()


def find_pair_match(arr, target):
    arr = sort_list(arr)
    num_elements = len(arr)

    for num in arr:
        match_target = target - num
        for other_num in arr[::-1]:
            if other_num < match_target:
                break
            elif other_num == match_target:
                return (num, other_num)

    return


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

    return


