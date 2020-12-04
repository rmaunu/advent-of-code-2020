import logging
import numpy as np

from .utils import read_list_file


logger = logging.getLogger(__name__)


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


def day_1(input_file):
    expenses = [int(expense) for expense in read_list_file(input_file)]
    match_pair = find_pair_match_2020(expenses)
    match_pair_multiple = match_pair[0] * match_pair[1]
    logger.info(f"The matching pair is {match_pair}, which is {match_pair_multiple} when multiplied")

    match_triplet = find_triplet_match_2020(expenses)
    match_triple_multiple = match_triplet[0] * match_triplet[1] * match_triplet[2]
    logger.info(f"The matching triplet is {match_triplet}, which is {match_triple_multiple} when multiplied")


