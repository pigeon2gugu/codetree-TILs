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

answer = ""
for i in range(idx+1) :
    answer += beforeElem[i]
    answer += str(cnts[i])

print(len(answer))
print(answer)