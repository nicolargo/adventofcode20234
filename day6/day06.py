def read_input(input_file):
    with open(input_file) as file:
        ret = file.read().strip().split("\n")
    return [list(line) for line in ret]


def print_puzzle(puzzle):
    print("=" * len(puzzle))
    for line in puzzle:
        print("".join(line))


def set_puzzle(puzzle, x, y, value):
    puzzle[y][x] = value


def get_puzzle(puzzle, x, y):
    return puzzle[y][x]


def get_guard(puzzle):
    for line_number, line in enumerate(puzzle):
        if "^" in line:
            return line.index("^"), line_number
    return None, None


def in_puzzle(puzzle, x, y):
    return 0 <= x < len(puzzle[0]) and 0 <= y < len(puzzle)


def count_path(puzzle):
    # Rotate the puzzle
    # print_puzzle(puzzle)
    guard = get_guard(puzzle)
    guard_direction = (0, -1)
    while in_puzzle(puzzle, guard[0], guard[1]):
        next_position = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])
        if get_puzzle(puzzle, next_position[0], next_position[1]) in ["#"]:
            # Turn right
            guard_direction = (-guard_direction[1], guard_direction[0])
            continue
        # Move forward
        # set_puzzle(puzzle, next_position[0], next_position[1], "^")
        set_puzzle(puzzle, guard[0], guard[1], "X")
        guard = next_position
    return sum([line.count("X") for line in puzzle])


def count_obs_loop(puzzle):
    # Rotate the puzzle
    guard = get_guard(puzzle)
    guard_direction = (0, -1)
    guard_path = set()
    while in_puzzle(puzzle, guard[0], guard[1]):
        if (guard, guard_direction) in guard_path:
            # We are in a loop... So return 0
            return True
        guard_path.add((guard, guard_direction))
        next_position = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])
        if not in_puzzle(puzzle, next_position[0], next_position[1]):
            return False
        if get_puzzle(puzzle, next_position[0], next_position[1]) in ["#", "O"]:
            # Turn right
            guard_direction = (-guard_direction[1], guard_direction[0])
            continue
        guard = next_position
    return False


def count_obs(puzzle, puzzle_path):
    ret = 0
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if get_puzzle(puzzle, x, y) != "^" and get_puzzle(puzzle_path, x, y) == "X":
                puzzle_to_test = [line.copy() for line in puzzle]
                set_puzzle(puzzle_to_test, x, y, "O")
                ret += count_obs_loop(puzzle_to_test)
    return ret


if __name__ == "__main__":
    input_file = "./input-day06.txt"

    # Part 1
    input_part1 = read_input(input_file)
    print(f"Part 1: {count_path(input_part1)}")

    # Part 2
    input_part2 = read_input(input_file)
    # The puzle solved in the part one is used to only test obs on path
    print(f"Part 2: {count_obs(input_part2, input_part1)}")
