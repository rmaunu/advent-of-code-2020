import logging
import re
import numpy as np

from .utils import read_list_file


logger = logging.getLogger(__name__)


def read_bag_instructions(input_file):
    lines = read_list_file(input_file)
    instructions = []
    for line in lines:
        instructions.append(parse_bag_instruction(line))
    return instructions

def parse_bag_instruction(line):
    instruction = re.search("^(.*)\sbags\scontain\s(.*)$", line.rstrip())
    this_bag_color = instruction.group(1)
    raw_bag_contains = instruction.group(2)
    if raw_bag_contains == 'no other bags.':
        raw_bag_contains = []
    else:
        raw_bag_contains = raw_bag_contains.split(", ")

    bag_contains = []
    for bag in raw_bag_contains:
        match = re.search("^(\d*)\s(.*)\sbag.*$", bag)
        bag_count = int(match.group(1))
        bag_color = match.group(2)
        bag_contains.append((bag_count, bag_color))

    return this_bag_color, bag_contains


def compile_bag_instructions(instructions):
    colors_contain = {}
    colors_held_by = {}
    for color, contains in instructions:
        colors_contain[color] = contains

        for count, other_color in contains:
            if other_color not in colors_held_by:
                colors_held_by[other_color] = set()
            colors_held_by[other_color].add(color)

    return colors_contain, colors_held_by


def possible_containers(colors_held_by, target_color):
    colors_can_hold_target = colors_held_by.get(target_color, set())
    all_colors_can_hold_target = colors_can_hold_target.copy()
    for color in colors_can_hold_target:
        all_colors_can_hold_target = all_colors_can_hold_target.union(
            possible_containers(colors_held_by, color))
    return all_colors_can_hold_target


def count_bags_contained(colors_contain, target_color):
    this_color_contains = colors_contain[target_color]
    num_total_bags = 0
    for count, color in this_color_contains:
        num_total_bags += count * (1 + count_bags_contained(colors_contain, color))
    return num_total_bags

def day_7(part, input_file):
    instructions = read_bag_instructions(input_file)
    colors_contain, colors_held_by = compile_bag_instructions(instructions)
    target_color = 'shiny gold'
    if part == 1:
        containing_colors = possible_containers(colors_held_by, target_color)
        num_containing_colors = len(containing_colors)
        logging.info(f"The '{target_color}' color can be held by {num_containing_colors} other colors")
    elif part == 2:
        num_total_bags = count_bags_contained(colors_contain, target_color)
        logging.info(f"The '{target_color}' bag will hold {num_total_bags} total bags")
