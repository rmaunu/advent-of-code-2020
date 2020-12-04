import logging

from .day_1 import day_1
from .day_2 import day_2
from .day_3 import day_3
from .day_4 import day_4


logger = logging.getLogger(__name__)


class AdventOfCode(object):

    def __init__(self):
        pass

    def run(self, day, part, input_file):
        method_to_call = getattr(AdventOfCode, f"day_{day}")
        method_to_call(part, input_file)
        return

    @staticmethod
    def day_1(part, input_file):
        day_1(part, input_file)

    @staticmethod
    def day_2(part, input_file):
        day_2(part, input_file)

    @staticmethod
    def day_3(part, input_file):
        day_3(part, input_file)

    @staticmethod
    def day_4(part, input_file):
        day_4(part, input_file)
