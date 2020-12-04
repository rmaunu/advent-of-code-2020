import re
import logging

from .utils import read_list_file


logger = logging.getLogger(__name__)


def read_password_file(input_file):
    lines = read_list_file(input_file)
    passwords_policies = [parse_password_policy(line) for line in lines]
    return passwords_policies


def parse_password_policy(line):
    match = re.search("(\d*)\-(\d*)\s(\w):\s(\w*)", line)
    policy = ([int(match.group(1)), int(match.group(2))], match.group(3))
    password = match.group(4)
    return password, policy


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


def day_2(part, input_file):
    passwords_policies = read_password_file(input_file)
    if part == 1:
        count_passwords_meet_policies = sum([
            does_password_meet_policy_count(password, policy)
            for password, policy in passwords_policies
        ])
        logger.info(f"{count_passwords_meet_policies} passwords meet their policy")
    elif part == 2:
        count_passwords_meet_policies = sum([
            does_password_meet_policy_position(password, policy)
            for password, policy in passwords_policies
        ])
        logger.info(f"{count_passwords_meet_policies} passwords meet their policy")
