with open("input.lst") as f:
    input = f.read().splitlines()

def check_corruption(line):
    corrupted = False
    score = 0
    score_map = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    opening_chars = ["(", "[", "{", "<"]
    closing_chars = [")", "]", "}", ">"]
    open_brackets = []

    for char in line:
        if char in opening_chars:
            open_brackets.append(char)
        elif char in closing_chars:
            if open_brackets[-1] != opening_chars[closing_chars.index(char)]:
                score = score_map[char]
                corrupted = True
                break
            else:
                open_brackets.pop()

    return(corrupted, score)

score = 0
for line in input:
    score += check_corruption(line)[1]

print(score)
