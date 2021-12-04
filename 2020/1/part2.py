with open("input.lst") as f:
    input = list(map(int, f.read().splitlines()))
for line in input:
    for line2 in input:
        for line3 in input:
            if line + line2 + line3 == 2020:
                entry1 = line
                entry2 = line2
                entry3 = line3

print(entry1 * entry2 * entry3)
