from collections import deque

n, k = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)] 
visited = [[False for _ in range(n)] for _ in range(n)]

q = deque()

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

def canMove(x, y) :
    return inRange(x, y) and graph[x][y] == 0 and visited[x][y] == False

def bfs() :
    while q :
        x, y = q.popleft()
        
        dxs, dys = [0, 1, 0 ,-1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy
            if canMove(nx, ny) :
                q.append((nx, ny))
                visited[nx][ny] = True

for i in range(len(points)) :
    x, y = points[i][0]-1, points[i][1]-1
    q.append((x, y))
    visited[x][y] = True

bfs()

cnt = sum([
    1
    for x in range(n)
    for y in range(n)
    if visited[x][y]
])

print(cnt)