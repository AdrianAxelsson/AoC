with open("input.lst") as f:
    input = f.read().splitlines()

ValidPasswords = 0

for line in input:
    NumOfChars = line.split(" ")[0]
    MinNum = int(NumOfChars.split("-")[0])
    MaxNum = int(NumOfChars.split("-")[1])
    Char = line.split(" ")[1].replace(":", "")
    Password = line.split(" ")[2]

    CharsMatched = 0
    for Character in Password:
        if Character == Char:
            CharsMatched += 1
    if CharsMatched >= MinNum and CharsMatched <= MaxNum:
        ValidPasswords += 1

print(ValidPasswords)