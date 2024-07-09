arr = list(map(int, input().split()))
n = 6
maxDiff = 1000000

ans = maxDiff

def getDiff(i, j, k) :
    point1 = arr[i] + arr[j] + arr[k]
    point2 = sum(arr) - point1
    return abs(point1 - point2)

for i in range(n - 2) :
    for j in range(i + 1, n - 1) :
        for k in range(j + 1, n) :
            ans = min(ans, getDiff(i, j, k))

print(ans)