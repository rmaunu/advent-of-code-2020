import logging
import re
import numpy as np

from .utils import read_list_file


logger = logging.getLogger(__name__)


TOTAL_ROW = 128
TOTAL_COLUMNS = 8


def read_seat_assignments(input_file):
    lines = read_list_file(input_file)
    seat_assignments = []
    for line in lines:
        seat_assignments.append(parse_seat_assignment(line.rstrip()))

    return seat_assignments

def parse_seat_assignment(seat_code):
    row_code = seat_code[:7]
    column_code = seat_code[7:]

    row_count = 0
    for i, instruction in enumerate(row_code):
        if instruction == 'B':
            row_count += TOTAL_ROW // (2 ** (i + 1))

    column_count = 0
    for i, instruction in enumerate(column_code):
        if instruction == 'R':
            column_count += TOTAL_COLUMNS // (2 ** (i + 1))

    return row_count, column_count

def seat_code(seat_assignment):
    row, column = seat_assignment
    return row * 8 + column

def day_5(part, input_file):
    seat_assignments = read_seat_assignments(input_file)
    if part == 1:
        max_seat_code = max([
            seat_code(seat_assignment) for seat_assignment in seat_assignments
        ])
        logger.info(f"The maximum assigned seat code is {max_seat_code}")
