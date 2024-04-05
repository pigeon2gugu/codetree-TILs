n, m = tuple(map(int, input().split()))
answer = [[0] * m for _ in range (n)]
def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < m

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

direction = 0
x, y = 0, 0
for i in range(1, n * m + 1) :

    answer[x][y] = i

    nx = x + dxs[direction]
    ny = y + dys[direction]

    if not inRange(nx, ny) or answer[nx][ny] != 0 :
        direction = (direction + 1) % 4

    x = x + dxs[direction]
    y = y + dys[direction]


for x in range(n) :
    for y in range(m) :
        print(answer[x][y], end = " ")
    print()