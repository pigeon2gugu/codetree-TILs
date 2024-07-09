n = int(input())
arr = ["n/a"] * 101
points = []

for _ in range(n):
    info = input().split()
    point = int(info[0])
    alpha = info[1]

    arr[point] = alpha
    points.append(point)

points = sorted(points)
maxVal = 0

for i in range(n - 1):
    tempPoint = 0
    gCount = 0
    hCount = 0
    for j in range(i, n):
        if arr[points[j]] == 'G':
            gCount += 1
        elif arr[points[j]] == 'H':
            hCount += 1
        
        if gCount == hCount or gCount == 0 or hCount == 0:
            tempPoint = j

    maxVal = max(maxVal, points[tempPoint] - points[i])

print(maxVal)