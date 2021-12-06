with open("input.lst") as f:
    input = list(map(int,f.read().split(",")))

days = 256

def map_fishes(input):
    fishes = {str(i): 0 for i in range(10)}
    for fish in input:
        fishes[str(fish)] += 1
    
    return fishes

fishes = map_fishes(input)

def new_day():
    for x in range(10):
        if x == 0:
            if(fishes[str(x)]) >= 1:
                fishes["9"] += fishes[str(x)]
                fishes["7"] += fishes[str(x)]
                fishes["0"] = 0
        else:
            fishes[str(x-1)] += fishes[str(x)]
            fishes[str(x)] -= fishes[str(x)]

for i in range(days):
    new_day()

print(sum(fishes.values()))
