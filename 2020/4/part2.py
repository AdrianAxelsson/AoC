import re

with open("input.lst") as f:
    input = f.read()

sanitized_input = re.sub('^\n', ';', input, flags=re.M).replace("\n", " ").replace(" ;", "\n").splitlines()
valid_passports = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for line in sanitized_input:
    invalid = 0
    for field in fields:
        if field not in line:
            invalid = 1
            break

    if invalid == 0:
        attribs = line.split(" ")
        attribdict = {}
        for attrib in attribs:
            key = attrib.split(":")[0]
            value = attrib.split(":")[1]
            attribdict[key] = value

        if int(attribdict["byr"]) >= 1920 and int(attribdict["byr"]) <= 2002:
            if int(attribdict["iyr"]) >= 2010 and int(attribdict["iyr"]) <= 2020:
                if int(attribdict["eyr"]) >= 2020 and int(attribdict["eyr"]) <= 2030:
                    if (attribdict["hgt"][-2:] == "cm" and int(attribdict["hgt"][:-2]) >= 150 and int(attribdict["hgt"][:-2]) <= 193) or (attribdict["hgt"][-2:] == "in" and int(attribdict["hgt"][:-2]) >= 59 and int(attribdict["hgt"][:-2]) <= 76):
                        if attribdict["hcl"][:1] == "#" and re.match("[0-9a-fA-F]{6}",attribdict["hcl"][1:]):
                            if attribdict["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                                if re.match("^[0-9]{9}$", attribdict["pid"]):
                                    print(attribdict["pid"])
                                    valid_passports += 1

print(valid_passports)
