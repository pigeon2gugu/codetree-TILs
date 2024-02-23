arr = list(map(int, input().split()))

idx = 0
for i in range(len(arr)) :
    if arr[i] == 0 :
        idx = i

for elem in arr[i-1::-1] :
    print(elem, end = " ")