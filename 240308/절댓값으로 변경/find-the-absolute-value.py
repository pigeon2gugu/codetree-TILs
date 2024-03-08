n = int(input())
arr = list(map(int, input().split()))

def toAbs(arr) :
    for i in range(len(arr)) :
        if arr[i] < 0 :
            arr[i] = arr[i] * -1


toAbs(arr)

for elem in arr :
    print(elem, end = " ")