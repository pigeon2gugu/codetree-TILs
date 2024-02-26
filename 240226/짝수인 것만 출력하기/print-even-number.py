n = int(input())
arr = list(map(int, input().split()))
newArr = []

for elem in arr :
    if elem % 2 == 0 :
        newArr.append(elem)

for elem in newArr :
    print(elem, end = " ")