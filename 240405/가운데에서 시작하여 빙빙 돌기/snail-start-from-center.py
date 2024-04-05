n = int(input())
answer = [[0] * n for _ in range(n)]

dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

direction = 0
x, y = n-1, n-1
for i in range(n*n, 0, -1) :

    answer[x][y] = i
    nx = x + dxs[direction]
    ny = y + dys[direction]

    if not inRange(nx, ny) or answer[nx][ny] != 0 :
        direction = (direction + 1) % 4

    x = x + dxs[direction]
    y = y + dys[direction]

for x in range(n) :
    for y in range(n) :
        print(answer[x][y], end = " ")
    print()