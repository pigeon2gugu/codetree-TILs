n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

maxCnt = 0
for i in range(n) :
    for j in range(n-2) :
        maxCnt = max(maxCnt, arr[i][j] + arr[i][j+1] + arr[i][j+2])

print(maxCnt)