import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

minDistance = sys.maxsize
x, y = tuple(points[0])

for i in range(1, n-1) :
    distance = 0
    tempX, tempY = tuple(points[i])
    points[i] = (x, y)
    for j in range(n-1) :
        distance += abs(points[j][0] - points[j+1][0]) + abs(points[j][1] - points[j+1][1])

    minDistance = min(distance, minDistance)
    points[i] = (tempX, tempY)

print(minDistance)