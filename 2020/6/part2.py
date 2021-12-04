with open("input.lst") as f:
    input = f.read().splitlines()

inputLen = len(input)
i = 0
answers = []
counts = 0
sum = 0

for line in input:
    for char in line:
        answers.append(char)
    counts += 1
    if i + 1 == inputLen:
        for answer in list(set(answers)):
            if answers.count(answer) == counts:
                sum += 1
        counts = 0
        answers = []
    elif input[i + 1] == "":
        for answer in list(set(answers)):
            if answers.count(answer) == counts:
                sum += 1
        counts = 0
        answers = []
    elif input[i] == "":
        counts = 0
        answers = []
    i += 1
    
print(sum)