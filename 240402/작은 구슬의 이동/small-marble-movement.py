n, t = tuple(map(int, input().split()))
y, x, d = tuple(input().split())

x = int(x) - 1
y = int(y) - 1

directions = {'U' : 2, 'D' : 1, 'R' : 3, 'L' : 0}

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

d = directions[d]

for tt in range(t):
    nx = x + dx[d]
    ny = y + dy[d]

    if not inRange(nx, ny):
        d = (3 - d) % 4  # 벽에 부딪혔을 때 방향을 반대로 변경
        nx = x + dx[d]
        ny = y + dy[d]

    if inRange(nx, ny):
        x, y = nx, ny

print(y + 1, x)