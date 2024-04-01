n, t = tuple(map(int, input().split()))
x, y, d = tuple(input().split())

x = int(x) - 1
y = int(y) - 1

directions = {'U' : 2, 'D' : 1, 'R' : 3, 'L' : 0}

dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

d = directions[d]
nx, ny = x, y

for tt in range(t) :

    if not inRange(nx, ny) :
        d = 3 - d
        nx = nx + dx[d]
        ny = ny + dy[d]

    nx = nx + dx[d]
    ny = ny + dy[d]


print(nx + 1, ny + 1)