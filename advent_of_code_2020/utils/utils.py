import logging


logger = logging.getLogger(__name__)


def read_list_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines
