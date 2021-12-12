with open("input.lst") as f:
    input = f.read().splitlines()

def map_grid(input):
    grid = [[] for _ in range(len(input))]
    y = 0
    for line in input:
        x = 0 
        for char in line:
            grid[y].append(int(char))
            x += 1
        y += 1
    return grid

def check_for_flash():
    for line in grid:
        for char in line:
            if char > 9:
                return(True)

def flash(y,x):
    if y > 0:
        if x > 0:
            grid[y-1][x-1] += 1
        if x < len(grid) - 1:
            grid[y-1][x+1] += 1
        grid[y-1][x] += 1
    if y < len(grid) - 1:
        if x > 0:
            grid[y+1][x-1] += 1       
        if x < len(grid) - 1:
            grid[y+1][x+1] += 1
        grid[y+1][x] += 1
    if x > 0:
        grid[y][x-1] += 1
    if x < len(grid) - 1:
        grid[y][x+1] += 1
    flashers.append([y,x])


flash_count = 0
steps = 100
grid = map_grid(input)

for n in range(steps):
    y = 0
    for line in grid:
        x = 0
        for char in line:
            grid[y][x] += 1
            x += 1
        y += 1

    flashers = []
    while check_for_flash():
        y = 0
        for line in grid:
            x = 0
            for char in line:
                if grid[y][x] > 9:
                    flash(y,x)
                x += 1
            y += 1
        for flasher in flashers:
            grid[flasher[0]][flasher[1]] = 0

    flash_count += len(flashers)

print(flash_count)
