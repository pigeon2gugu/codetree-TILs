arr = list(map(int, input().split()))

idx = len(arr)-1

for i in range(len(arr)) :
    if arr[i] == 0 :
        idx = i

for elem in arr[idx-1::-1] :
    print(elem, end = " ")