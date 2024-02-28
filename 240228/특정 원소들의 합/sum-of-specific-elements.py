arr = [list(map(int, input().split())) for _ in range(4)]

sumVal = 0
for i in range(4) :
    for j in range(i+1) :
        sumVal += arr[i][j]

print(sumVal)