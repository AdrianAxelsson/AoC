with open("input.lst") as f:
    input = f.read().splitlines()

lines = {
    "x_lines": [],
    "y_lines": []
}

for line in input:
    split_line = line.split(" -> ")
    if split_line[0].split(",")[0] == split_line[1].split(",")[0]: ## y-line
        lines["y_lines"].append(line)
    elif split_line[0].split(",")[1] == split_line[1].split(",")[1]: ## x-line
        lines["x_lines"].append(line)

def create_grid(size):
    grid = [[] for _ in range(size)]

    for i in range(size):
        for g in grid:
            grid[i].append(0)

    return grid

def calc_line_pos(line, axis):
    if axis == "x":
        pos = []
        y_pos = int(line.split(" -> ")[0].split(",")[1])
        x1 = int(line.split(" -> ")[0].split(",")[0])
        x2 = int(line.split(" -> ")[1].split(",")[0])
        if x1 < x2:
            x_range = range(x1, x2 + 1)
            for i in x_range:
                pos.append([i, y_pos])
        else:
            x_range = range(x1, x2 - 1, -1)
            for i in x_range:
                pos.append([i, y_pos])
    elif axis == "y":
        pos = []
        x_pos = int(line.split(" -> ")[0].split(",")[0])
        y1 = int(line.split(" -> ")[0].split(",")[1])
        y2 = int(line.split(" -> ")[1].split(",")[1])
        if y1 < y2:
            y_range = range(y1, y2 + 1)
            for i in y_range:
                pos.append([x_pos, i])
        else:
            x_range = range(y1, y2 - 1, -1)
            for i in x_range:
                pos.append([x_pos, i])
    return(pos)

def dot_grid(coords):
    for coord in coords:
        x = coord[0]
        y = coord[1]
        grid[y][x] += 1

def count_overlap():
    points = 0
    for row in grid:
        for val in row:
            if val >= 2:
                points += 1
    return points

grid = create_grid(1000)

for line in lines["x_lines"]:
    dot_grid(calc_line_pos(line, "x"))
for line in lines["y_lines"]:
    dot_grid(calc_line_pos(line, "y"))

print(count_overlap())