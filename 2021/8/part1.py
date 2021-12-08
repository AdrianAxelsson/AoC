with open("input.lst") as f:
    input = f.read().splitlines()

digit_count = 0
for line in input:
    output = line.split(" | ")[1]
    for value in output.split(" "):
        if len(value) in [2, 3, 4, 7]:
            digit_count += 1

print(digit_count)
