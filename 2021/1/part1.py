with open("input.lst") as f:
    measurements = list(map(int, f.read().splitlines()))
x = 0
i = 0
for m in measurements:
    if i == 0:
        i = i + 1
        continue
    if m > measurements[i - 1]:
        x = x + 1
    i = i + 1
print(x)