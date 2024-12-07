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
    # print_puzzle(input)
    guard = get_guard(input)
    guard_direction = (0, -1)
    while True:
        # print_puzzle(puzzle)
        next_position = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])
        if not in_puzzle(puzzle, next_position[0], next_position[1]):
            # Guard no more in puzzle
            set_puzzle(puzzle, guard[0], guard[1], "X")
            break
        elif get_puzzle(puzzle, next_position[0], next_position[1]) in ["#", "O"]:
            # Turn right
            guard_direction = (-guard_direction[1], guard_direction[0])
        else:
            # Move forward
            set_puzzle(puzzle, next_position[0], next_position[1], "^")
            set_puzzle(puzzle, guard[0], guard[1], "X")
            guard = next_position
    return sum([line.count("X") for line in puzzle])


# Read input file
input = read_input("./input-example-day06.txt")


# Part 1
print(f"Part 1: {count_path(input)}")

# Part 2
print("Part 2: ")
