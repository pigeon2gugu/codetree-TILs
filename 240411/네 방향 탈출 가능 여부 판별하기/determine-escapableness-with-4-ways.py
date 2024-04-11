from collections import deque

n, m = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < m 

def canMove(x, y) :
    return inRange(x, y) and graph[x][y] == 1 and visited[x][y] == 0

def push(x, y) :
    visited[x][y] = 1
    q.append((x, y))

def bfs() :
    while q :
        x, y = q.popleft()        
        dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy
            if canMove(nx, ny) :
                push(nx, ny)


push(0, 0)
bfs()

print(visited[n-1][m-1])