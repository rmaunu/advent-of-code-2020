import logging
from copy import deepcopy

from .utils import read_list_file


logger = logging.getLogger(__name__)


def read_seat_file(input_file):
    lines = read_list_file(input_file)
    seat_base = [[-1 if c == "." else 0 for c in line.rstrip()] for line in lines]
    return seat_base


def find_surrounding_seats_adjacent(current_seats, row, space):
    min_row = max(0, row - 1)
    max_row = min(len(current_seats) - 1, row + 1)
    min_space = max(0, space - 1)
    max_space = min(len(current_seats[0]) - 1, space + 1)

    surrounding_seats = []
    for i in range(min_row, max_row + 1):
        for j in range(min_space, max_space + 1):
            if i == row and j == space:
                continue

            space_value = current_seats[i][j]
            if space_value == -1:
                continue
            else:
                surrounding_seats.append(space_value)

    return surrounding_seats


def find_surrounding_seats_expansive(current_seats, row, space):
    surrounding_seats = []
    num_rows = len(current_seats)
    num_columns = len(current_seats[0])
    for row_direction in (-1, 0, 1):
        for column_direction in (-1, 0, 1):
            if row_direction == 0 and column_direction == 0:
                continue

            next_row = row
            next_space = space
            next_seat = -1
            while next_seat == -1:
                next_row += row_direction
                next_space += column_direction
                if next_row < 0 or next_row >= num_rows:
                    break
                if next_space < 0 or next_space >= num_columns:
                    break
                next_seat = current_seats[next_row][next_space]

            if next_seat != -1:
                surrounding_seats.append(next_seat)

    return surrounding_seats


def update_seat_status(seat_status, surrounding_seats, max_occupied):
    if seat_status == 0:
        if sum(surrounding_seats) == 0:
            return 1
    elif seat_status == 1:
        num_occupied_seats = sum(seat for seat in surrounding_seats)
        if num_occupied_seats >= max_occupied:
            return 0

    return seat_status


def run_seating_step(current_seats, max_occupied, seat_check='adjacent'):
    next_seats = deepcopy(current_seats)
    num_updates = 0
    for i, row in enumerate(next_seats):
        for j, space in enumerate(row):
            if space == -1:
                continue
            if seat_check == 'adjacent':
                surrounding_seats = find_surrounding_seats_adjacent(
                    current_seats, i, j)
            else:
                surrounding_seats = find_surrounding_seats_expansive(
                    current_seats, i, j)
            next_seat_status = update_seat_status(
                space, surrounding_seats, max_occupied)
            if next_seat_status != space: num_updates += 1
            next_seats[i][j] = next_seat_status

    return next_seats, num_updates


def day_11(part, input_file):
    seat_base = read_seat_file(input_file)
    if part == 1:
        max_occupied = 4
        next_seats, num_updates = run_seating_step(seat_base, max_occupied)
        logger.info(f"Next step updated {num_updates} seats")

        while num_updates > 0:
            next_seats, num_updates = run_seating_step(next_seats, max_occupied)
            logger.info(f"Next step updated {num_updates} seats")

        num_occupied_seats = sum(seat == 1 for row in next_seats for seat in row)
        logger.info(f"There are {num_occupied_seats} occupied seats in the plane")
    elif part == 2:
        max_occupied = 5
        next_seats, num_updates = run_seating_step(
            seat_base, max_occupied, seat_check='expansive')
        logger.info(f"Next step updated {num_updates} seats")

        while num_updates > 0:
            next_seats, num_updates = run_seating_step(
                next_seats, max_occupied, seat_check='expansive')
            logger.info(f"Next step updated {num_updates} seats")

        num_occupied_seats = sum(seat == 1 for row in next_seats for seat in row)
        logger.info(f"There are {num_occupied_seats} occupied seats in the plane")
