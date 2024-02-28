arr = list(map(int, input().split()))
newArr = []

for elem in arr :
    if elem == 999 or elem == -999 :
        break
    
    newArr.append(elem)

print(f"{max(newArr)} {min(newArr)}")