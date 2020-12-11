import logging
import re
import numpy as np

from .utils import read_int_list_file, find_pair_match, sort_list


logger = logging.getLogger(__name__)

PREAMBLE_SIZE = 25


def find_first_invalid_value(values, preamble_size=PREAMBLE_SIZE):
    num_values = len(values)

    for i in range(preamble_size, num_values):
        target = values[i]
        previous_values = values[i - preamble_size:i]
        pair = find_pair_match(previous_values, target)
        if pair is None:
            return target


def find_contiguous_set_sum(values, target):
    num_values = len(values)
    for set_size in range(2, num_values):
        for i in range(num_values - set_size):
            subset_values = values[i:i + set_size]
            if sum(subset_values) == target:
                return subset_values


def day_9(part, input_file):
    values = read_int_list_file(input_file)
    target = find_first_invalid_value(values)
    if part == 1:
        logger.info(f"Failed to find pair summing to {target}")
    elif part == 2:
        previous_answer = target
        subset_values = find_contiguous_set_sum(values, previous_answer)
        sorted_subset_values = sort_list(subset_values)
        target = sorted_subset_values[0] + sorted_subset_values[-1]
        logger.info(f"The encryption weakness is {target}")
