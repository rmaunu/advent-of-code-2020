import logging

from .utils import day1, day2, day3


logger = logging.getLogger(__name__)


class AdventOfCode(object):

    def __init__(self):
        pass

    def run(self, task, input_file):
        method_to_call = getattr(AdventOfCode, f"command_{task}")
        method_to_call(input_file)
        return

    @staticmethod
    def command_1(input_file):
        day1(input_file)

    @staticmethod
    def command_2(input_file):
        day2(input_file)

    @staticmethod
    def command_3(input_file):
        day3(input_file)
