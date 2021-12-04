with open("input.lst") as f:
    input = f.read().splitlines()

inputLen = len(input)
i = 0
answers = []
sum = 0

for line in input:
    for char in line:
        if char not in answers:
            answers.append(char)
    if i + 1 == inputLen:
        sum += len(answers)
    elif input[i + 1] == "":
        sum += len(answers)
        answers = []
    i += 1
print(sum)