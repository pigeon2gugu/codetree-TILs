n, m = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < m

def canMove(x, y) :
    if not inRange(x, y) :
        return False

    if graph[x][y] == 1 or visited[x][y] :
        return False

    return True

def dfs(x, y) :
    visited[x][y] = True
    for dx, dy in zip(dxs, dys) :
        nx, ny = x + dx, y + dy
        if canMove(nx, ny) :
            dfs(nx, ny)

    return visited[n-1][m-1]

if dfs(0, 0) :
    print(1)
else :
    print(0)