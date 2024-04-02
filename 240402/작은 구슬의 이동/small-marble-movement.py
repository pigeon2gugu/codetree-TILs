n, t = tuple(map(int, input().split()))
y, x, d = tuple(input().split())

x = int(x) - 1
y = int(y) - 1

directions = {'U' : 2, 'D' : 1, 'R' : 3, 'L' : 0}

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

d = directions[d]
nx, ny = x, y

for tt in range(t) :

    nx = nx + dx[d]
    ny = ny + dy[d]

    if not inRange(nx, ny) :
        d = 3 - d
        nx = nx + dx[d]
        ny = ny + dy[d]


print(ny + 1, nx + 1)