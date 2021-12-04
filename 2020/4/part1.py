import re

with open("input.lst") as f:
    input = f.read()

sanitized_input = re.sub('^\n', ';', input, flags=re.M).replace("\n", "").replace(";", "\n").splitlines()
valid_passports = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for line in sanitized_input:
    invalid = 0
    for field in fields:
        if field not in line:
            invalid = 1
            break

    if invalid == 0:
        valid_passports += 1

print(valid_passports)
