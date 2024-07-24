n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
ans = 40001 * 40001

for i in range(n):
    minx = 40001
    miny = 40001
    maxx = 0
    maxy = 0
    for j in range(n):
        if i == j:
            continue

        minx = min(minx, arr[j][0])
        maxx = max(maxx, arr[j][0])
        miny = min(miny, arr[j][1])
        maxy = max(maxy, arr[j][1])

    ans = min(ans, (maxx - minx) * (maxy - miny))

print(ans)