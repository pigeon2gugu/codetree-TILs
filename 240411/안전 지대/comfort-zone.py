import sys

n, m = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
sys.setrecursionlimit(3000)

areas = []

def inRange(x, y):
    return 0 <= x < n and 0 <= y < m 

def canMove(x, y, k):
    return inRange(x, y) and graph[x][y] > k and not visited[x][y]

def dfs(x, y, k):
    visited[x][y] = True

    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if canMove(nx, ny, k):
            dfs(nx, ny, k)


maxHeight = max(max(row) for row in graph)
for h in range(1, maxHeight + 1):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if canMove(i, j, h):
                cnt += 1
                dfs(i, j, h)

    areas.append(cnt)

maxCount = max(areas)
maxIndex = areas.index(maxCount) + 1

print(maxIndex, maxCount)