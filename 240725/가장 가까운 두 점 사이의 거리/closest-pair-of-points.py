import sys

n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
ans = sys.maxsize

for i in range(n) :
    for j in range(n) :
        if i == j :
            continue

        ans = min(ans, (arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)

print(ans)