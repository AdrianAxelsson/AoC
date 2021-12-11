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

def complete_line_score(line):
    score = 0
    score_map = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    opening_chars = ["(", "[", "{", "<"]
    closing_chars = [")", "]", "}", ">"]
    open_brackets = []

    for char in line:
        if char in opening_chars:
            open_brackets.append(char)
        elif char in closing_chars:
            open_brackets.pop()
    for char in reversed(open_brackets):
        score *= 5
        score += score_map[closing_chars[opening_chars.index(char)]]
    
    return(score)

incompete_lines = []
for line in input:
    if check_corruption(line)[0] == False:
        incompete_lines.append(line)

scores = []
for line in incompete_lines:
    scores.append(complete_line_score(line))
scores.sort()
print(scores[int((len(scores) - 1) / 2)])
