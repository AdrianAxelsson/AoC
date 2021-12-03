with open("input.lst") as f:
    measurements = list(map(int, f.read().splitlines()))
x = 0
i = 0
win = [0]
for m in measurements:
    if i + 3 > len(measurements):
        break
    win.append(m + measurements[i + 1] + measurements[i + 2])
    if i == 0:
        i = i + 1
        continue
    if win[i] > win[i - 1]:
        x = x + 1
    i = i + 1
print(x)
