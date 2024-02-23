arr = list(map(int, input().split()))
start, end = arr[0], arr[1]

cnt = 0
for i in range(start, end + 1) :
    temp = 0
    for j in range(1, i) :
        if i % j == 0 :
            temp += j
    if temp == i :
        cnt += 1

print(cnt)