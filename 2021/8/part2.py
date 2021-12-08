with open("input.lst") as f:
    input = f.read().splitlines()

def get_output(entry):
    num_mapping = [0 for i in range(10)]
    char_mapping = {}
    pattern, output = entry.split(" | ")
    for value in pattern.split(" "):
        if len(value) == 2:
            num_mapping[1] = value
        elif len(value) == 3:
            num_mapping[7] = value
        elif len(value) == 4:
            num_mapping[4] = value
        elif len(value) == 7:
            num_mapping[8] = value
    for char in num_mapping[7]:
        if char not in num_mapping[1]:
            char_mapping["a"] = char
    for value in pattern.split(" "):
        if num_mapping[1][0] in value and num_mapping[1][1] in value and len(value) == 5:
            num_mapping[3] = value
            for char in num_mapping[4]:
                if char not in num_mapping[3]:
                    char_mapping["b"] = char
    for value in pattern.split(" "):
        if len(value) == 5 and char_mapping["b"] in value:
            num_mapping[5] = value
            for char in num_mapping[1]:
                if char in value:
                    char_mapping["f"] = char
                else:
                    char_mapping["c"] = char
    for char in num_mapping[4]:
        if char not in [char_mapping["b"], char_mapping["c"], char_mapping["f"]]:
            char_mapping["d"] = char
    num_mapping[6] = num_mapping[8].replace(char_mapping["c"], "")
    num_mapping[0] = num_mapping[8].replace(char_mapping["d"], "")
    num_mapping[2] = num_mapping[8].replace(char_mapping["b"], "").replace(char_mapping["f"], "")
    for value in pattern.split(" "):
        if len(value) == 6 and char_mapping["c"] in value and char_mapping["d"] in value:
            num_mapping[9] = value

    for i in range(len(num_mapping)):
        sorted_num = sorted(num_mapping[i])
        num_mapping[i] = "".join(sorted_num)
    ret_val = []
    for value in output.split(" "):
        sorted_output = sorted(value)
        ret_val.append(str(num_mapping.index("".join(sorted_output))))

    return int("".join(ret_val))

sum = 0
for line in input:
    sum += get_output(line)

print(sum)
