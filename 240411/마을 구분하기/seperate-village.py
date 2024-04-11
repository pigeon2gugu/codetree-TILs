n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
people = []

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def canMove(x, y):
    return inRange(x, y) and graph[x][y] == 1 and not visited[x][y]

def dfs(x, y):
    visited[x][y] = True
    count = 1

    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if canMove(nx, ny):
            count += dfs(nx, ny)
             
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            people.append(dfs(i, j))

print(len(people))
for p in sorted(people):
    print(p)