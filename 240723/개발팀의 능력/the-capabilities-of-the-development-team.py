import sys
n = 5
arr = list(map(int, input().split()))
ans = sys.maxsize

def getDiff(i, j, k, l) :
    point1 = arr[i] + arr[j]
    point2 = arr[k] + arr[l]
    point3 = sum(arr) - point1 - point2

    if point1 == point2 or point1 == point3 or point2 == point3 :
        return sys.maxsize

    maxPoint = max(max(point1, point2), point3)
    minPoint = min(min(point1, point2), point3)

    return (maxPoint - minPoint)

for i in range(n-1) :
    for j in range(i + 1, n) :
        for k in range(n-1) :
            for l in range(k + 1, n) :
                if i == k or i == l or j == k or j == l :
                    continue

                ans = min(ans, getDiff(i, j, k, l))


if ans == sys.maxsize :
    ans = -1

print(ans)