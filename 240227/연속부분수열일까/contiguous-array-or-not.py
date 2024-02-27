lenA, lenB = tuple(map(int, input().split()))
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))


idx = -1
tf = "Yes"
for elem in arrB :

    if elem in arrA :
        temp = arrA.index(elem)
        arrA[temp] = -1
    else :
        tf = "No"
        break

    if idx != -1 and temp != idx + 1 :
        tf = "No"
        break

    idx = temp


print(tf)