with open("input.lst") as f:
    input = list(map(int, f.read().splitlines()))
for line in input:
    for line2 in input:
        if line + line2 == 2020:
            entry1 = line
            entry2 = line2

print(entry1 * entry2)
