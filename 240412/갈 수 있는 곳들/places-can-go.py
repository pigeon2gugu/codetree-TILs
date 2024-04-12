from collections import deque
import sys

sys.setrecursionlimit(10000)

n, k = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)] 
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0

q = deque()

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

def canMove(x, y) :
    return inRange(x, y) and graph[x][y] == 0 and visited[x][y] == False

def bfs() :
    global cnt
    while q :
        x, y = q.popleft()
        visited[x][y] = True
        
        dxs, dys = [0, 1, 0 ,-1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy
            if canMove(nx, ny) :
                q.append((nx, ny))
                cnt += 1
                bfs()


for i in range(len(points)) :
    x, y = points[i][0]-1, points[i][1]-1

    if not visited[x][y] :
        cnt += 1

    q.append((x, y))
    bfs()

print(cnt)