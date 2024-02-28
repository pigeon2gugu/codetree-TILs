n = int(input())
arr = list(map(int, input().split()))
newArr = [arr[0]]

for elem in arr[1::] :
    if elem in newArr :
        newArr.pop(newArr.index(elem))
        continue
    newArr.append(elem)


print(max(newArr))