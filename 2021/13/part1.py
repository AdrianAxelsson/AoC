with open("input.lst") as f:
    input = f.read().splitlines()


def get_instructions(input):
    instructions = []
    for line in input:
        if "fold along" in line:
            instructions.append(line)
    return(instructions)

def get_coords(input):
    coords = []
    for line in input:
        if line != "" and line[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            coords.append(line)
    return(coords)

def generate_grid(input):
    x_len = 0
    y_len = 0
    for line in input:
        x, y = line.split(",")
        if int(x) > x_len:
            x_len = int(x)
        if int(y) > y_len:
            y_len = int(y)
    grid = [["." for _ in range(x_len + 1)] for _ in range(y_len + 1)]
    return grid

def map_grid(grid, coords):
    for line in coords:
        x, y = line.split(",")
        grid[int(y)][int(x)] = "#"
    return

def print_grid(grid):
    for line in grid:
        print(*line)

def count_dots(grid):
    return(sum(x.count("#") for x in grid))

def fold_grid(grid, instruction):
    inst = instruction.split(" ")[2]
    axis, pos = inst.split("=")
    if axis == "y":
        y = len(grid) - int(pos) - 2
        for line in grid[int(pos) + 1:]:
            x = 0
            for char in line:
                if char == "#":
                    grid[y][x] = "#"
                x += 1
            y -= 1
        for i in range(int(pos) + 1):
            grid.pop()
    elif axis == "x":
        y = 0
        for line in grid:
            x = len(grid[0]) - int(pos) - 2
            for char in line[int(pos) + 1:]:
                if char == "#":
                    grid[y][x] = "#"
                x -= 1
            y += 1
        y = 0
        for line in grid:
            for i in range(int(pos) + 1):
                grid[y].pop()
            y += 1
    return



grid = generate_grid(get_coords(input))
coords = get_coords(input)
instructions = get_instructions(input)
folds = 1

map_grid(grid, coords)

for i in range(folds):
    fold_grid(grid, instructions[i])

print(count_dots(grid))