n, t = tuple(map(int, input().split()))
stmts = input()
nums = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y = n // 2, n // 2

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

ans = nums[x][y]
direction = 0
for s in stmts :

    if s == 'L' :
        direction = (direction - 1) % 4
    elif s == 'R' :
        direction = (direction + 1) % 4
    elif s == 'F' :
        nx = x + dxs[direction]
        ny = y + dys[direction]

        if inRange(nx, ny) :
            ans += nums[nx][ny]
            x = nx
            y = ny

print(ans)