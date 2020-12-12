import logging

from .day_1 import day_1
from .day_2 import day_2
from .day_3 import day_3
from .day_4 import day_4
from .day_5 import day_5
from .day_6 import day_6
from .day_7 import day_7
from .day_8 import day_8
from .day_9 import day_9
from .day_10 import day_10
from .day_11 import day_11
from .day_12 import day_12


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

    @staticmethod
    def day_5(part, input_file):
        day_5(part, input_file)

    @staticmethod
    def day_6(part, input_file):
        day_6(part, input_file)

    @staticmethod
    def day_7(part, input_file):
        day_7(part, input_file)

    @staticmethod
    def day_8(part, input_file):
        day_8(part, input_file)

    @staticmethod
    def day_9(part, input_file):
        day_9(part, input_file)

    @staticmethod
    def day_10(part, input_file):
        day_10(part, input_file)

    @staticmethod
    def day_11(part, input_file):
        day_11(part, input_file)

    @staticmethod
    def day_12(part, input_file):
        day_12(part, input_file)
