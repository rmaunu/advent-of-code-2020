import logging


from .utils import read_int_list_file, comb, sort_list


logger = logging.getLogger(__name__)


def calculate_joltage_differences(joltages, device_joltage):
    sorted_adaptor_joltages = sort_list(joltages)
    sorted_adaptor_joltages = [0] + sorted_adaptor_joltages + [device_joltage]
    joltage_differences = [
        high_joltage - low_joltage
        for low_joltage, high_joltage in zip(
            sorted_adaptor_joltages[:-1], sorted_adaptor_joltages[1:]
        )
    ]
    return joltage_differences


def calculate_adaptor_paths(joltages, device_joltage, max_difference):
    sorted_adaptor_joltages = sort_list(joltages)
    sorted_adaptor_joltages.append(device_joltage)

    num_paths_at_adaptor = {}
    num_paths_at_adaptor[0] = 1
    for adaptor in sorted_adaptor_joltages:
        paths_at_adaptor = sum([
            num_paths_at_adaptor.get(adaptor - i, 0)
            for i in range(1, max_difference + 1)
        ])
        num_paths_at_adaptor[adaptor] = paths_at_adaptor

    return num_paths_at_adaptor[device_joltage]


def day_10(part, input_file):
    adaptor_joltages = read_int_list_file(input_file)
    device_joltage = max(adaptor_joltages) + 3

    if part == 1:
        joltage_differences = calculate_joltage_differences(
            adaptor_joltages, device_joltage)
        joltage_difference_counts = {1: 0, 2: 0, 3: 0}
        for difference in joltage_differences:
            joltage_difference_counts[difference] += 1

        joltage_difference_product = joltage_difference_counts[3] * joltage_difference_counts[1]
        logger.info(f"The solution is {joltage_difference_product}")
    elif part == 2:
        combinatorics = calculate_adaptor_paths(adaptor_joltages, device_joltage, 3)
        logger.info(f"There are {combinatorics} viable combinations")
