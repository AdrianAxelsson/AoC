with open("input.lst") as f:
    input = f.read().splitlines()

InputLen = len(input[0])
OxygenData = input[:]
CO2Data = input[:]

for i in range(InputLen):
    NrOf0 = 0
    NrOf1 = 0
    for line in OxygenData:
        if int(line[i]) == 0:
            NrOf0 = NrOf0 + 1
        elif int(line[i]) == 1:
            NrOf1 = NrOf1 + 1

    LinesToRemove = []
    if NrOf1 > NrOf0:
        for line in OxygenData:
            if int(line[i]) == 0:
                LinesToRemove.append(line)
    elif NrOf1 < NrOf0:
        for line in OxygenData:
            if int(line[i]) == 1:
                LinesToRemove.append(line)
    elif NrOf1 == NrOf0:
         for line in OxygenData:
            if int(line[i]) == 0:
                LinesToRemove.append(line)

    for line in LinesToRemove:
        OxygenData.remove(line)

OxygenDataByteStr = ''.join(OxygenData)
OxygenDataDecInt = int(OxygenDataByteStr, 2)

for i in range(InputLen):
    NrOf0 = 0
    NrOf1 = 0
    if (len(CO2Data) == 1):
        continue
    for line in CO2Data:
        if int(line[i]) == 0:
            NrOf0 = NrOf0 + 1
        elif int(line[i]) == 1:
            NrOf1 = NrOf1 + 1

    LinesToRemove = []
    if NrOf1 > NrOf0:
        for line in CO2Data:
            if int(line[i]) == 1:
                LinesToRemove.append(line)
    elif NrOf1 < NrOf0:
        for line in CO2Data:
            if int(line[i]) == 0:
                LinesToRemove.append(line)
    elif NrOf1 == NrOf0:
         for line in CO2Data:
            if int(line[i]) == 1:
                LinesToRemove.append(line)

    for line in LinesToRemove:
        CO2Data.remove(line)

CO2DataByteStr = ''.join(CO2Data)
CO2DataDecInt = int(CO2DataByteStr, 2)

print(CO2DataDecInt * OxygenDataDecInt)