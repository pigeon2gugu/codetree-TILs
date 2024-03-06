s = input()
l = len(s)

shiftString = s
print(shiftString)
for _ in range(l) :
    shiftString = shiftString[-1] + shiftString[:-1]
    print(shiftString)