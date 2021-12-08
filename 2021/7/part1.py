import statistics

with open("input.lst") as f:
    input = list(map(int,f.read().split(",")))

median = statistics.median(input)
fuel = 0
for crab in input:
    fuel += abs(median - crab)

print(fuel)
