import logging
import numpy as np

from .utils import read_list_file


logger = logging.getLogger(__name__)


ORIENTATION = {
    "N": np.matrix([0, 1]).T,
    "S": np.matrix([0, -1]).T,
    "E": np.matrix([1, 0]).T,
    "W": np.matrix([-1, 0]).T,
}
CLOCKWISE_ROTATION = np.matrix([[0, 1], [-1, 0]])


def read_instruction_file(input_file):
    lines = read_list_file(input_file)
    instructions = [(line[0], int(line[1:].rstrip())) for line in lines]
    return instructions


def update_orientation(current_orientation, direction, value):
    rotation = CLOCKWISE_ROTATION
    if direction == 'L': rotation = rotation * -1

    num_rotations = value // 90
    next_orientation = current_orientation
    for i in range(num_rotations):
        next_orientation = np.dot(rotation, next_orientation)

    return next_orientation


def update_position(current_position, orientation, value):
    next_position = value * orientation + current_position
    return next_position


def run_instructions(
    instructions,
    starting_orientation=ORIENTATION["E"],
    starting_position=np.matrix([0, 0]).T,
    is_waypoint=False,
):
    current_orientation = starting_orientation
    current_position = starting_position

    for direction, value in instructions:
        if direction in ('L', 'R'):
            current_orientation = update_orientation(
                current_orientation, direction, value)
        else:
            if direction == 'F':
                move_direction = current_orientation
                current_position = update_position(
                    current_position, move_direction, value)
            else:
                move_direction = ORIENTATION[direction]
                if is_waypoint:
                    current_orientation = update_position(
                        current_orientation, move_direction, value)
                else:
                    current_position = update_position(
                        current_position, move_direction, value)

    return current_position


def day_12(part, input_file):
    instructions = read_instruction_file(input_file)
    if part == 1:
        position = run_instructions(instructions)
        manhattan_distance = np.sum(np.abs(position))
        logger.info(f"You are {manhattan_distance} from your starting position")
    elif part == 2:
        position = run_instructions(
            instructions,
            starting_orientation=np.matrix([10, 1]).T,
            is_waypoint=True,
        )
        manhattan_distance = np.sum(np.abs(position))
        logger.info(f"You are {manhattan_distance} from your starting position")
