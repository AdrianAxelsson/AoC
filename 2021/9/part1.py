with open("input.lst") as f:
    input = f.read().splitlines()

x_len = len(input[0]) - 1
y_len = len(input) - 1
risk = 0
for line in input:
    i = 0
    for char in line:
        if input.index(line) == 0:
            if i == 0:
                if (int(char) < int(line[i + 1])) and (int(char) < int(input[input.index(line) + 1][i])):
                    risk += int(char) + 1
            elif i == x_len:
                if (int(char) < int(line[i - 1])) and (int(char) < int(input[input.index(line) + 1][i])):
                    risk += int(char) + 1
            else:
                if (int(char) < int(line[i + 1])) and (int(char) < int(line[i - 1])) and (int(char) < int(input[input.index(line) + 1][i])):
                    risk += int(char) + 1
        elif input.index(line) == y_len:
            if i == 0:
                if (int(char) < int(line[i + 1])) and (int(char) < int(input[input.index(line) - 1][i])):
                    risk += int(char) + 1
            elif i == x_len:
                if (int(char) < int(line[i - 1])) and (int(char) < int(input[input.index(line) - 1][i])):
                    risk += int(char) + 1
            else:
                if (int(char) < int(line[i + 1])) and (int(char) < int(line[i - 1])) and (int(char) < int(input[input.index(line) - 1][i])):
                    risk += int(char) + 1
        else:
            if i == 0:
                if (int(char) < int(line[i + 1])) and (int(char) < int(input[input.index(line) - 1][i])) and (int(char) < int(input[input.index(line) + 1][i])):
                    risk += int(char) + 1
            elif i == x_len:
                if (int(char) < int(line[i - 1])) and (int(char) < int(input[input.index(line) - 1][i])) and (int(char) < int(input[input.index(line) + 1][i])):
                    risk += int(char) + 1
            else:
                if (int(char) < int(line[i + 1])) and (int(char) < int(line[i - 1])) and (int(char) < int(input[input.index(line) - 1][i])) and (int(char) < int(input[input.index(line) + 1][i])):
                    risk += int(char) + 1
        i += 1

print(risk)