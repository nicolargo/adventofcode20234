from itertools import combinations


def read_input(input_file):
    with open(input_file) as file:
        ret = file.read().strip().split("\n")
    return [list(line) for line in ret]


def print_puzzle(puzzle):
    print("=" * len(puzzle))
    for line in puzzle:
        print("".join(line))


def set_puzzle(puzzle, x, y, value):
    if x < 0 or y < 0 or x >= len(puzzle[0]) or y >= len(puzzle):
        return
    puzzle[y][x] = value


def get_puzzle(puzzle, x, y):
    return puzzle[y][x]


def get_antennas(puzzle):
    """Return a dict of antennas positions"""
    ret = dict()
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            antenna_freq = get_puzzle(puzzle, x, y)
            if antenna_freq == ".":
                # No antenna
                continue
            if antenna_freq in ret:
                ret[antenna_freq].append((x, y))
            else:
                ret[antenna_freq] = [(x, y)]
    return ret


def get_antinodes(antennas):
    ret = set()
    for freq in antennas:
        # Define all combinations
        comb = list(combinations(antennas[freq], 2))
        for c in comb:
            # Compute direction
            # Ex: ((8, 1), (5, 2)) => (3, -1)
            direction = tuple((b - a) for a, b in zip(*c))
            # Compute antinodes thanks to  direction
            # Ex: ((8, 1), (5, 2)) => ((2, 3), (11, 0))
            # Ex: ((5, 2), (7, 3)) => ((3, 1), (9, 4))
            antinodes = (
                (c[0][0] - direction[0], c[0][1] - direction[1]),
                (c[1][0] + direction[0], c[1][1] + direction[1]),
            )
            ret.update(antinodes)
    return ret


def part1(puzzle):
    # print_puzzle(puzzle)
    # Get antennas position in the puzzle as a dict:
    # key = frequency
    # values: list of position
    antennas = get_antennas(puzzle)
    # For each frequency, identify the antinodes
    antinodes = get_antinodes(antennas)
    for a in antinodes:
        set_puzzle(puzzle, a[0], a[1], "#")
    return sum(line.count("#") for line in puzzle)


def part2(puzzle):
    pass


if __name__ == "__main__":
    input_file = "./input-day08.txt"

    # Part 1
    input_part1 = read_input(input_file)
    print(f"Part 1: {part1(input_part1)}")

    # Part 2
    input_part2 = read_input(input_file)
    print(f"Part 2: {part2(input_part2)}")
