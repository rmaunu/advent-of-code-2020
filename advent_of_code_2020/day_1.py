import logging

from .utils import read_list_file, find_pair_match, find_triplet_match


logger = logging.getLogger(__name__)


def find_pair_match_2020(arr):
    return find_pair_match(arr, 2020)


def find_triplet_match_2020(arr):
    return find_triplet_match(arr, 2020)


def day_1(part, input_file):
    expenses = [int(expense) for expense in read_list_file(input_file)]
    if part == 1:
        match_pair = find_pair_match_2020(expenses)
        match_pair_multiple = match_pair[0] * match_pair[1]
        logger.info(f"The matching pair is {match_pair}, which is {match_pair_multiple} when multiplied")
    elif part == 2:
        match_triplet = find_triplet_match_2020(expenses)
        match_triple_multiple = match_triplet[0] * match_triplet[1] * match_triplet[2]
        logger.info(f"The matching triplet is {match_triplet}, which is {match_triple_multiple} when multiplied")


