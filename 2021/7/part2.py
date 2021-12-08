import statistics

with open("input.lst") as f:
    input = list(map(int,f.read().split(",")))

mean = int(statistics.mean(input))
fuel = 0
for crab in input:
    steps = abs(mean - crab)
    for step in range(steps):
        fuel += step + 1
        
print(fuel)
