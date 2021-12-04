with open("input.lst") as f:
    input = f.read().splitlines()

Pos = [0, 0]
TreeHits = 0

PatternLength = len(input[0])
PatternDepth = len(input)

def checkCollision(Pos):
    if input[Pos[1]][Pos[0]] == "#":
        return 1
    else:
        return 0

def move(Pos):
    Pos[0] += 1
    Pos[1] += 1
    if Pos[0] == PatternLength:
        Pos[0] = 0

    Pos[0] += 1
    if Pos[0] == PatternLength:
        Pos[0] = 0

    Pos[0] += 1
    if Pos[0] == PatternLength:
        Pos[0] = 0
    
    TreeHit = checkCollision(Pos)

    return Pos, TreeHit
    
for i in range(PatternDepth - 1):
    Pos, TreeHit = move(Pos)
    TreeHits = TreeHits + TreeHit

print(TreeHits)
