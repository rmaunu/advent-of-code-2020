import logging
import re

from .utils import read_list_file


logger = logging.getLogger(__name__)


def read_instructions_file(input_file):
    lines = read_list_file(input_file)
    instructions = []
    for line in lines:
        instruction = line.split()

        command = instruction[0]

        value = instruction[1]
        if value[0] == '+':
            value = int(value[1:])
        else:
            value = -1 * int(value[1:])

        instructions.append((command, value))

    return instructions

def do_instruction(instruction, current_line, accumulator):
    command, value = instruction

    if command == 'nop':
        next_line = current_line + 1
    elif command == 'acc':
        next_line = current_line + 1
        accumulator += value
    elif command == 'jmp':
        next_line =  current_line + value

    return next_line, accumulator

def test_instructions(instructions):
    num_instructions = len(instructions)
    seen_lines = set()
    current_line = 0
    accumulator = 0

    is_infinite_loop = False
    while True:
        instruction = instructions[current_line]
        next_line, accumulator = do_instruction(instruction, current_line, accumulator)

        if next_line in seen_lines:
            is_infinite_loop = True
            break
        else:
            seen_lines.add(current_line)

        if next_line < num_instructions:
            current_line = next_line
        else:
            break

    return is_infinite_loop, current_line, accumulator


def debug_instructions(instructions):
    for debug_line in range(len(instructions)):
        debug_instructions = instructions.copy()
        debug_instruction = debug_instructions[debug_line]
        debug_command, debug_value = debug_instruction

        if debug_command == 'acc':
            continue
        elif debug_command == 'jmp':
            debug_command = 'nop'
        elif debug_command == 'nop':
            debug_command = 'jmp'

        debug_instructions[debug_line] = (debug_command, debug_value)
        is_infinite_loop, current_line, accumulator = test_instructions(debug_instructions)
        if not is_infinite_loop:
            logger.info(f"Corrupt line is {debug_line}. The correct accumulator value is {accumulator}")


def day_8(part, input_file):
    instructions = read_instructions_file(input_file)
    if part == 1:
        is_infinite_loop, current_line, accumulator = test_instructions(instructions)
        logger.info(f'Infinite loop at line {current_line}!!! The accumulator is at {accumulator}.')
    elif part == 2:
        debug_instructions(instructions)
