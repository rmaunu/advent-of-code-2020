import logging


from .utils import read_int_list_file, comb, sort_list


logger = logging.getLogger(__name__)


def calculate_joltage_differences(joltages, device_joltage):
    sorted_adaptor_joltages = sort_list(joltages)
    sorted_adaptor_joltages = [0] + sorted_adaptor_joltages + [device_joltage]
    print(sorted_adaptor_joltages)
    joltage_differences = [
        high_joltage - low_joltage
        for low_joltage, high_joltage in zip(
            sorted_adaptor_joltages[:-1], sorted_adaptor_joltages[1:]
        )
    ]
    return joltage_differences


def calculate_joltage_combinatorics(joltage_differences):
    single_joltage_difference_block_sizes = []
    current_size = 0
    for difference in joltage_differences:
        if difference != 1 and current_size > 0:
            single_joltage_difference_block_sizes.append(current_size)
            current_size = 0
        elif difference == 1:
            current_size += 1

    total_combinatorics = 1
    for block_size in single_joltage_difference_block_sizes:
        total_combinatorics *= adaptor_combinatorics(block_size, 3)

    return total_combinatorics


def adaptor_combinatorics(block_size, max_difference):
    if block_size <= max_difference:
        combinatorics = 2 ** (block_size - 1)
    else:
        num_max_difference_blocks = block_size // max_difference
        max_missing_adaptors = \
            block_size // max_difference * (max_difference - 1) + \
            (block_size % max_difference - 1)

        combinatorics = 1
        for i in range(1, max_missing_adaptors + 1):
            if i < max_difference:
                combinatorics += comb(block_size - 1, i)
            else:
                continue  # need to implement case where num missing adaptors can violate the max difference rule

    return combinatorics


def day_10(part, input_file):
    adaptor_joltages = read_int_list_file(input_file)
    device_joltage = max(adaptor_joltages) + 3
    joltage_differences = calculate_joltage_differences(
        adaptor_joltages, device_joltage)

    if part == 1:
        joltage_difference_counts = {1: 0, 2: 0, 3: 0}
        for difference in joltage_differences:
            joltage_difference_counts[difference] += 1

        joltage_difference_product = joltage_difference_counts[3] * joltage_difference_counts[1]
        logger.info(f"The solution is {joltage_difference_product}")
    elif part == 2:
        combinatorics = calculate_joltage_combinatorics(joltage_differences)
        logger.info(f"There are {combinatorics} viable combinations")
