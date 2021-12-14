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

def process_rules(neighbors, rules):
    neighbors_to_add = {}
    char_count = {}
    for char in chars_in_input:
        char_count[char] = 0
    for rule in rules:
        neighbors_to_add[rule[0]] = 0
    for rule in rules:
        if neighbors[rule[0]] > 0:
            neighbors_to_add[rule[0][0]+rule[1]] += neighbors[rule[0]]
            neighbors_to_add[rule[1]+rule[0][1]] += neighbors[rule[0]]
            neighbors_to_add[rule[0]] -= neighbors[rule[0]]
            char_count[rule[1]] += neighbors[rule[0]]

    for rule in rules:
        neighbors[rule[0]] += neighbors_to_add[rule[0]]
        
    return(neighbors, char_count)

def calc_polymer(char_count):
    result = max(char_count.values()) - min(char_count.values())
    return(result)

steps = 40
rules = get_rules(input)
template = get_template(input)

char_count = {}
chars_in_input = set()
for rule in rules:
    chars_in_input.add(rule[1])
for char in chars_in_input:
    char_count[char] = 0
for char in template:
    char_count[char] = template.count(char)

neighbors = {}
for rule in rules:
        neighbors[rule[0]] = 0
for rule in rules:
    if template.count(rule[0]) > 0:
        neighbors[rule[0]] += template.count(rule[0])

for i in range(steps):
    neighbors, new_chars = process_rules(neighbors, rules)
    for char in new_chars:
        char_count[char] += new_chars[char]

print(calc_polymer(char_count))
