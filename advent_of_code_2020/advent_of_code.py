import logging

from .utils import day_1, day_2, day_3


logger = logging.getLogger(__name__)


class AdventOfCode(object):

    def __init__(self):
        pass

    def run(self, task, input_file):
        method_to_call = getattr(AdventOfCode, f"day_{task}")
        method_to_call(input_file)
        return

    @staticmethod
    def day_1(input_file):
        day_1(input_file)

    @staticmethod
    def day_2(input_file):
        day_2(input_file)

    @staticmethod
    def day_3(input_file):
        day_3(input_file)
