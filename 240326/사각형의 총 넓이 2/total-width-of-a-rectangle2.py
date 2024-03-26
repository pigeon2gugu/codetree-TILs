n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
maxL = 10 * 100
coordinate = [([0] * (maxL * 2 + 1)) for _ in range((maxL * 2 + 1))]

for p in points :
    x1, y1, x2, y2 = p[0] + maxL, p[1] + maxL, p[2] + maxL, p[3] + maxL
    for i in range(x1, x2) :
        for j in range(y1, y2) :
            coordinate[i][j] = 1

cnt = 0
for x in range(len(coordinate[0])) :
    for y in range(len(coordinate)) :
        if coordinate[x][y] == 1 :
            cnt += 1


print(cnt)