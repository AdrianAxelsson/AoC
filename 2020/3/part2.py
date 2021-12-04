with open("input.lst") as f:
    input = f.read().splitlines()

PatternLength = len(input[0])
PatternDepth = len(input)

def checkCollision(Pos):
    if input[Pos[1]][Pos[0]] == "#":
        return 1
    else:
        return 0

def move(Pos, x_len, y_len):
    for i in range(x_len):
        Pos[0] += 1
        if Pos[0] == PatternLength:
            Pos[0] = 0
    for i in range(y_len):
        Pos[1] += 1
        if Pos[1] == PatternDepth:
            Pos[1] -= 1
            return Pos, 0

    TreeHit = checkCollision(Pos)

    return Pos, TreeHit

def testSlope(x_len, y_len):
    TreeHits = 0
    Pos = [0, 0]
    for i in range(PatternDepth - 1):
        Pos, TreeHit = move(Pos, x_len, y_len)
        TreeHits = TreeHits + TreeHit
    return TreeHits

Result = (testSlope(1, 1) * testSlope(3, 1) * testSlope(5, 1) * testSlope(7, 1) * testSlope(1, 2))
print(Result)
