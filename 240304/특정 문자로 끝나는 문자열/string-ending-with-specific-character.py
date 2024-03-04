arr = []

while True :
    temp = input()
    if len(temp) == 1 :
        s = temp
        break
    else :
        arr.append(temp)

for elem in arr :
    if elem[-1] == s :
        print(elem)