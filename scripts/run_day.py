import argparse
import logging

from advent_of_code_2020.advent_of_code import AdventOfCode


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    parser.add_argument("part", type=int)

    parser.set_defaults(func=main)
    return parser.parse_args()


def main():
    args = parse_args()
    logger.info(f"day = {args.day}")
    advent = AdventOfCode()
    advent.run(args.day, args.part, f"/data/day{args.day}.dat")


if __name__ == "__main__":
    main()
