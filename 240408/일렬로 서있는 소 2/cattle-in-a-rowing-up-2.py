n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(len(arr)-2) :
    for j in range(i + 1, len(arr)-1) :
        for k in range(j + 1, len(arr)) :
            if arr[i] <= arr[j] <= arr[k] :
                cnt += 1

print(cnt)