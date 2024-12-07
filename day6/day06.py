def read_input(input_file):
    with open(input_file) as file:
        return file.read().strip().split("\n")


def print_puzzle(puzzle):
    print("=" * len(puzzle))
    for p in puzzle:
        print(p)


def rotate_puzzle_90r(puzzle):
    ret = [["." for _ in range(len(puzzle))] for _ in range(len(puzzle))]
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            ret[i][j], ret[j][i] = puzzle[j][i], puzzle[i][j]
    for row in ret:
        row.reverse()
    return ["".join(r) for r in ret]


def count_path(puzzle):
    # Rotate the puzzle
    puzzle = rotate_puzzle_90r(puzzle)
    while any(["^" in i for i in puzzle]):
        for line_number, line in enumerate(puzzle):
            if "^" in line:
                guard_pos = line.index("^")
                if "#" in line[guard_pos:]:
                    # Look for the wall
                    wall_pos = guard_pos + line[guard_pos:].index("#")
                    # Move the guard up to the wall
                    # and add a X to the path
                    puzzle[line_number] = (
                        line[:guard_pos]
                        + "X" * (wall_pos - guard_pos - 1)
                        + "^"
                        + line[wall_pos:]
                    )
                    # Rotate the puzzle
                    puzzle = rotate_puzzle_90r(puzzle)
                    puzzle = rotate_puzzle_90r(puzzle)
                    puzzle = rotate_puzzle_90r(puzzle)
                    break
                else:
                    puzzle[line_number] = line[:guard_pos] + "X" * (
                        len(line) - guard_pos
                    )
                    break
    return sum([line.count("X") for line in puzzle])


# Read input file
input = read_input("./input-example-day06.txt")


# Part 1
print(f"Part 1: {count_path(input)}")

# Part 2
print("Part 2: ")
