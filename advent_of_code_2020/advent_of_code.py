import logging

from .utils import module_fuel


logger = logging.getLogger(__name__)


class AdventOfCode(object):

    def __init__(self):
        pass

    def run(self, task, input_file):
        method_to_call = getattr(AdventOfCode, f"command_{task}")
        method_to_call(input_file)

    @staticmethod
    def command_1(input_file):
        masses = []
        with open(input_file, "r") as f:
            lines = f.readlines()
            masses = [int(mass) for mass in lines]
        print(masses)
        fuel = sum([module_fuel(mass) for mass in masses])
        logger.info(fuel)
