import logging

from .day_1 import day_1
from .day_2 import day_2
from .day_3 import day_3
from .day_4 import day_4


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

    @staticmethod
    def day_4(input_file):
        day_4(input_file)
