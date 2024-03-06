a = input()
b = input()

newA = ""
for elem in a :
    if elem.isdigit() :
        newA += elem

newB = ""
for elem in b :
    if elem.isdigit() :
        newB += elem


a = int(newA)
b = int(newB)

print(a + b)