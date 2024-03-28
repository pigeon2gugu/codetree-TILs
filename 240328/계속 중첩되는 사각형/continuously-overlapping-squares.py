n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]

offset = 100
maxL = offset * 2 + 1
areas = [[-1] * maxL for _ in range(maxL)]

for idx, r in enumerate(rects, start = 1) :
    x1, y1, x2, y2 = r[0] + offset, r[1] + offset, r[2] + offset, r[3] + offset

    for i in range(x1, x2) :
        for j in range(y1, y2) :
            areas[i][j] = idx % 2


cnt = 0
for x in range(maxL) :
    for y in range(maxL) :
        if areas[x][y] == 0 :
            cnt += 1


print(cnt)