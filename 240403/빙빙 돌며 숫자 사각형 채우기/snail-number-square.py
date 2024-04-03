n, m = tuple(map(int, input().split()))
answer = [[0] * m for _ in range(n)]

dc, dr = [1, 0, -1, 0], [0, 1, 0, -1]
r, c = 0, 0

def inRange(r, c) :
    return r >= 0 and r < n and c >= 0 and c < m

direction = 0
for i in range(1, n * m + 1) :

    answer[r][c] = i

    nr = r + dr[direction]
    nc = c + dc[direction]

    if not inRange(nr, nc) or answer[nr][nc] != 0 :
        direction = (direction + 1) % 4
    
    r = r + dr[direction]
    c = c + dc[direction]

for i in range(n) :
    for j in range(m) :
        print(answer[i][j], end = " ")
    print()