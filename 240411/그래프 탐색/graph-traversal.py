verticeNum, edgeNum = tuple(map(int, input().split()))
graph = [[] for _ in range(verticeNum + 1)]
visited = [False for _ in range(verticeNum + 1)]
cnt = 0

for _ in range(edgeNum) :
    start, end = tuple(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)

def dfs(vertex) :
    for currentVertex in graph[vertex] :
        if not visited[currentVertex] :
            visited[currentVertex] = True
            dfs(currentVertex)

dfs(1)

for idx, v in enumerate(visited) :
    if v and idx != 1 :
        cnt += 1

print(cnt)