with open("input.lst") as f:
    input = f.read().splitlines()

def map_grid(input):
    grid = [[] for _ in range(len(input))]
    for line in input:
        i = 0 
        for char in line:
            grid[input.index(line)].append(char)
            i += 1
    return grid

def check_neighbors(x, y, grid):
    x_len = len(input[0]) - 1
    y_len = len(input) - 1
    neighbors = {
        "Value": grid[y][x],
        "U": None,
        "D": None,
        "L": None,
        "R": None
    }
    if y == 0:
        if x == 0:
            neighbors["D"] = int(grid[y + 1][x])
            neighbors["R"] = int(grid[y][x + 1])        
        elif x == x_len:
            neighbors["D"] = int(grid[y + 1][x])
            neighbors["L"] = int(grid[y][x - 1])
        else:
            neighbors["D"] = int(grid[y + 1][x])
            neighbors["R"] = int(grid[y][x + 1])
            neighbors["L"] = int(grid[y][x - 1])

    elif y == y_len:
        if x == 0:
            neighbors["U"] = int(grid[y - 1][x])
            neighbors["R"] = int(grid[y][x + 1])
        elif x == x_len:
            neighbors["U"] = int(grid[y - 1][x])
            neighbors["L"] = int(grid[y][x - 1])
        else:
            neighbors["U"] = int(grid[y - 1][x])
            neighbors["R"] = int(grid[y][x + 1])
            neighbors["L"] = int(grid[y][x - 1])
    else:
        if x == 0:
            neighbors["U"] = int(grid[y - 1][x])
            neighbors["D"] = int(grid[y + 1][x])
            neighbors["R"] = int(grid[y][x + 1])        
        elif x == x_len:
            neighbors["U"] = int(grid[y - 1][x])
            neighbors["D"] = int(grid[y + 1][x])
            neighbors["L"] = int(grid[y][x - 1])
        else:
            neighbors["U"] = int(grid[y - 1][x])
            neighbors["D"] = int(grid[y + 1][x])
            neighbors["R"] = int(grid[y][x + 1])
            neighbors["L"] = int(grid[y][x - 1])
    return neighbors

def test_lowpoint(location):
    lowpoint = True
    for key in location:
        if key == "Value":
            continue
        elif location[key] == None:
            continue
        if int(location["Value"]) >= int(location[key]):
            lowpoint = False
    return lowpoint, location["Value"]

def calc_basin_size(lowpoint):
    size = 0
    sus_neighbors = [[lowpoint["y"], lowpoint["x"], int(lowpoint["value"])]]
    popped = []

    while sus_neighbors:
        neighbors = check_neighbors(sus_neighbors[0][1], sus_neighbors[0][0], grid)
        for key in neighbors:
            if key == "Value":
                continue
            elif neighbors[key] == None:
                continue
            if int(neighbors[key]) < 9:
                if key == "L":
                    if [int(sus_neighbors[0][0]), int(sus_neighbors[0][1]) - 1, neighbors[key]] not in sus_neighbors and [int(sus_neighbors[0][0]), int(sus_neighbors[0][1]) - 1, int(neighbors[key])] not in popped:
                        sus_neighbors.append([int(sus_neighbors[0][0]), int(sus_neighbors[0][1]) - 1, int(neighbors[key])])
                if key == "R":
                    if [int(sus_neighbors[0][0]), int(sus_neighbors[0][1]) + 1, int(neighbors[key])] not in sus_neighbors and [int(sus_neighbors[0][0]), int(sus_neighbors[0][1]) + 1, int(neighbors[key])] not in popped:
                        sus_neighbors.append([int(sus_neighbors[0][0]), int(sus_neighbors[0][1]) + 1, int(neighbors[key])])
                if key == "U":
                    if [int(sus_neighbors[0][0]) - 1, int(sus_neighbors[0][1]), int(neighbors[key])] not in sus_neighbors and [int(sus_neighbors[0][0]) - 1, int(sus_neighbors[0][1]), int(neighbors[key])] not in popped:
                        sus_neighbors.append([int(sus_neighbors[0][0]) - 1, int(sus_neighbors[0][1]), int(neighbors[key])])
                if key == "D":
                    if [int(sus_neighbors[0][0]) + 1, int(sus_neighbors[0][1]), int(neighbors[key])] not in sus_neighbors and [int(sus_neighbors[0][0]) + 1, int(sus_neighbors[0][1]), int(neighbors[key])] not in popped:
                        sus_neighbors.append([int(sus_neighbors[0][0]) + 1, int(sus_neighbors[0][1]), int(neighbors[key])])
        popped.append(sus_neighbors.pop(0))
        size += 1
    return size

def get_lowpoints():
    lowpoints = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            lowpoint, value = test_lowpoint(check_neighbors(x, y, grid))
            if lowpoint == True:
                lowpoints.append({
                    "value": value,
                    "x": x,
                    "y": y
                })
    return lowpoints

def get_largest_basins():
    basins = []
    for lowpoint in lowpoints:
        basins.append(calc_basin_size(lowpoint))
    basins.sort()
    return basins[-3:]

grid = map_grid(input)
lowpoints = get_lowpoints()

result = 1
for basin in get_largest_basins():
    result = result * basin
print(result)
