with open("input.lst") as f:
    input = f.read().splitlines()

def get_rules(input):
    rules = []
    for line in input:
        if "->" in line:
            rules.append(line.split(" -> "))
    return(rules)

def get_template(input):
    return input[0]

def process_rules(template, rules):
    temp_template = list(template)
    for i in range(len(template) - 1):
        for rule in rules:
            if template[i]+template[i+1] == rule[0]:
                temp_template.insert(i + i + 1, rule[1])
    template = "".join(temp_template)
    return(template)

def calc_polymer(template):
    unique_chars = list(set(template))
    chars_count = {}
    for char in unique_chars:
        chars_count[char] = template.count(char)
    result = max(chars_count.values()) - min(chars_count.values())
    return(result)

rules = get_rules(input)
template = get_template(input)
steps = 10
for i in range(steps):
    template = process_rules(template, rules)

result = calc_polymer(template)
print(result)
