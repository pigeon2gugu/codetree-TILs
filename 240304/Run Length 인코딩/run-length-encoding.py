s = input()

beforeElem = [s[0]]
idx = 0
cnts = [1]

for elem in s[1:] :
    if beforeElem[idx] == elem :
        cnts[idx] += 1
    else :
        idx += 1
        beforeElem.append(elem)
        cnts.append(1)

print((idx+1)*2)
for i in range(idx+1) :
    print(beforeElem[i], end = "")
    print(cnts[i], end = "")