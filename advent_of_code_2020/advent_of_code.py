import logging

from .utils import find_pair_match_2020, find_triplet_match_2020, read_list_file, read_password_file, does_password_meet_policy_count, does_password_meet_policy_position


logger = logging.getLogger(__name__)


class AdventOfCode(object):

    def __init__(self):
        pass

    def run(self, task, input_file):
        method_to_call = getattr(AdventOfCode, f"command_{task}")
        method_to_call(input_file)
        return

    @staticmethod
    def command_1(input_file):
        expenses = [int(expense) for expense in read_list_file(input_file)]
        match_pair = find_pair_match_2020(expenses)
        match_pair_multiple = match_pair[0] * match_pair[1]
        logger.info(f"The matching pair is {match_pair}, which is {match_pair_multiple} when multiplied")

        match_triplet = find_triplet_match_2020(expenses)
        match_triple_multiple = match_triplet[0] * match_triplet[1] * match_triplet[2]
        logger.info(f"The matching triplet is {match_triplet}, which is {match_triple_multiple} when multiplied")

    @staticmethod
    def command_2(input_file):
       passwords_policies = read_password_file(input_file)
       count_passwords_meet_policies = sum([
           # does_password_meet_policy_count(password, policy)
           does_password_meet_policy_position(password, policy)
           for password, policy in passwords_policies
       ])
       logger.info(f"{count_passwords_meet_policies} passwords meet their policy")
