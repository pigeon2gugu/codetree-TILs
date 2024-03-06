a, b = tuple(input().split())

newA = ""
for elem in a :
    if elem.isdigit() :
        newA += elem
    else :
        break

newB = ""
for elem in b :
    if elem.isdigit() :
        newB += elem
    else :
        break

newA, newB = int(newA), int(newB)

print(newA + newB)