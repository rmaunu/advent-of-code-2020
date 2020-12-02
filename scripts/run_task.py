import argparse
import logging

from advent_of_code_2020.advent_of_code import AdventOfCode


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", type=int)

    parser.set_defaults(func=main)
    return parser.parse_args()


def main():
    args = parse_args()
    logger.info(f"task = {args.task}")
    advent = AdventOfCode()
    advent.run(args.task, f"/data/day{args.task}.dat")


if __name__ == "__main__":
    main()
