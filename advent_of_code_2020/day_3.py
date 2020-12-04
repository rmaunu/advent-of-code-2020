import numpy as np
import logging

from .utils import read_list_file


logger = logging.getLogger(__name__)


def read_forest_file(input_file):
    lines = read_list_file(input_file)
    forest_base = [[1 if c == "#" else 0 for c in line.rstrip()] for line in lines]
    return forest_base

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


def day_3(part, input_file):
    forest_base = read_forest_file(input_file)
    if part  == 1:
        count_trees = count_trees_toboggan(forest_base, [1, 3])
        logger.info(f"Your tobogggan hits {count_trees} trees")

    elif part == 2:
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
