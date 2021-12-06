with open("input.lst") as f:
    input = list(map(int,f.read().split(",")))

days = 80

def new_day():
    i = 0
    for fish in input:
        if fish == 0:
            input[i] = 6
            input.append(9)
        else:
            input[i] -= 1
        i += 1
    return None

for i in range(days):
    new_day()

print(len(input))