offset = 1000
maxL = offset * 2 + 1
n = 2
rects = [tuple(map(int, input().split())) for _ in range(n)]
area = [[0] * maxL for _ in range(maxL)]

for i, (x1, y1, x2, y2) in enumerate(rects, start = 1) :
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset

    for x in range(x1, x2) :
        for y in range(y1, y2) :
            area[x][y] = i
            
minX = maxL
maxX = -maxL
minY = maxL
maxY = -maxL

cnt = 0
for x in range(maxL) :
    for y in range(maxL) :
        if area[x][y] == 1 :
            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)
            cnt += 1

if cnt == 0 :
    print(0)
else :
    print((maxX - minX + 1) * (maxY - minY + 1))