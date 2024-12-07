import re
from itertools import product
from operator import add, mul


def read_input(input_file):
    with open(input_file) as file:
        return [
            list(map(int, re.findall("\\d+", line)))
            for line in file.read().strip().split("\n")
        ]


def part1(puzzle, operations=(add, mul)):
    ret = []
    for equation in puzzle:
        value, calibration_first, *calibration_other = equation
        # Build a list with all combinations between operations & calibration_other
        combinations = list(
            tuple(zip(calibration_other, combo))
            for combo in product(operations, repeat=len(calibration_other))
        )
        # Search a good combination
        for combination in combinations:
            current = calibration_first
            for ops in combination:
                current = ops[1](current, ops[0])
            if current == value:
                ret.append(value)
                break

    return sum(ret)


def concatenation(a, b):
    return int(str(a) + str(b))


def part2(puzzle):
    return part1(puzzle, operations=(add, mul, concatenation))


if __name__ == "__main__":
    input_file = "./input-day07.txt"

    # Part 1
    input_part1 = read_input(input_file)
    print(f"Part 1: {part1(input_part1)}")

    # Part 2
    input_part2 = read_input(input_file)
    print(f"Part 2: {part2(input_part2)}")
