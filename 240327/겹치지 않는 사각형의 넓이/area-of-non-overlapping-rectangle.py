n = 3
rects = [tuple(map(int, input().split())) for _ in range(n)]
offset = 1000
maxL = offset * 2 + 1
area = [[0] * maxL for _ in range(maxL)]

for i in range(n) :
    rect = rects[i]
    x1, y1, x2, y2 = rect[0] + offset, rect[1] + offset, rect[2] + offset, rect[3] + offset

    if i == 2 :
        for j in range(x1, x2) :
            for k in range(y1, y2) :
                area[j][k] = 0
    else :
        for j in range(x1, x2) :
            for k in range(y1, y2) :
                area[j][k] = 1


cnt = 0
for x in range(maxL) :
    for y in range(maxL) :
        if area[x][y] == 1 :
            cnt += 1

print(cnt)