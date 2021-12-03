with open("input.lst") as f:
    input = f.read().splitlines()

h_pos = 0
d_pos = 0
aim = 0

for command in input:
    action = command.split(" ")[0]
    units = command.split(" ")[1]
    if action == 'up':
        aim = aim - int(units)
    elif action == 'down':
        aim = aim + int(units)
    elif action == 'forward':
        h_pos = h_pos + int(units)
        d_pos = d_pos + (int(units) * aim)

print(h_pos * d_pos)