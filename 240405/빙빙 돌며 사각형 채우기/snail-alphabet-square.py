n, m = tuple(map(int, input().split()))
answer = [[0] * m for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0
direction = 0

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < m

num = ord('A')
for i in range(num, num + (n * m)) :

    newNum = i
    if newNum > ord('Z') :
        newNum -= (ord('Z') - ord('A'))

    answer[x][y] = chr(newNum)

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