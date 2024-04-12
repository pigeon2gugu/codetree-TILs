from collections import deque

n, k = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()

x, y = tuple(map(int, input().split()))
x -= 1
y -= 1
value = graph[x][y]
maxValue = 0

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

def canMove(x, y) :
    global value
    return inRange(x, y) and graph[x][y] < value and visited[x][y] == False

def bfs() :
    global value
    global maxValue

    while q :
        x, y = q.popleft()
        dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy
            if canMove(nx, ny) :
                q.append((nx, ny))
                maxValue = max(maxValue, graph[nx][ny])
                visited[nx][ny] = True

def movePivot() :
    global n, x, y, maxValue, visited, value
    isFind = False

    for i in range(n) :
        if isFind :
            break
        for j in range(n) :
            if visited[i][j] == True and graph[i][j] == maxValue :
                x, y = i, j
                isFind = True
                break

    visited = [[False for _ in range(n)] for _ in range(n)]
    maxValue = 0
    value = graph[x][y]
            

for _ in range(k) :
    q.append((x, y))
    bfs()
    movePivot()
    

print(x+1, y+1)