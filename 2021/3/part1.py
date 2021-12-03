with open("input.lst") as f:
    input = f.read().splitlines()

InputLen = len(input[0])
GammaByteArr = []
EpsilonByteArr = []
for i in range(InputLen):
    NrOf0 = 0
    NrOf1 = 0
    for line in input:
        if int(line[i]) == 0:
            NrOf0 = NrOf0 + 1
        elif int(line[i]) == 1:
            NrOf1 = NrOf1 + 1
    if NrOf0 > NrOf1:
        GammaByteArr.append("0")
    else:
        GammaByteArr.append("1")

for i in range(InputLen):
    NrOf0 = 0
    NrOf1 = 0
    for line in input:
        if int(line[i]) == 0:
            NrOf0 = NrOf0 + 1
        elif int(line[i]) == 1:
            NrOf1 = NrOf1 + 1
    if NrOf0 > NrOf1:
        EpsilonByteArr.append("1")
    else:
        EpsilonByteArr.append("0")

GammaByteStr = ''.join(GammaByteArr)
EpsilonBytestr = ''.join(EpsilonByteArr)
GammaDecInt = int(GammaByteStr, 2)
EpsilonDecInt = int(EpsilonBytestr, 2)

print(EpsilonDecInt * GammaDecInt)