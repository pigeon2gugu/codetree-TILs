n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]
offset = 100
maxL = offset * 2 + 1
area = [[0] * maxL for _ in range(maxL)]

for r in rects :
    x1, x2, y1, y2 = r[0] + offset, r[0] + offset + 8, r[1] + offset, r[1] + offset + 8

    for x in range(x1, x2) :
        for y in range(y1, y2) :
            area[x][y] = 1

cnt = 0
for x in range(maxL) :
    for y in range(maxL) :
        if area[x][y] == 1:
            cnt += 1

print(cnt)