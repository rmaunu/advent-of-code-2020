import logging

from .utils import find_pair_match_2020, find_triplet_match_2020


logger = logging.getLogger(__name__)


class AdventOfCode(object):

    def __init__(self):
        pass

    def run(self, task, input_file):
        method_to_call = getattr(AdventOfCode, f"command_{task}")
        method_to_call(input_file)
        return

    @staticmethod
    def read_file(input_file):
        with open(input_file, "r") as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def command_1(input_file):
        expenses = [int(expense) for expense in AdventOfCode.read_file(input_file)]
        match_pair = find_pair_match_2020(expenses)
        match_pair_multiple = match_pair[0] * match_pair[1]
        logger.info(f"The matching pair is {match_pair}, which is {match_pair_multiple} when multiplied")

        match_triplet = find_triplet_match_2020(expenses)
        match_triple_multiple = match_triplet[0] * match_triplet[1] * match_triplet[2]
        logger.info(f"The matching triplet is {match_triplet}, which is {match_triple_multiple} when multiplied")

