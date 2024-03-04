s = input()
newS = s[1::2]

for elem in newS[-1::-1] :
    print(elem, end = "")