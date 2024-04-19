n, m = tuple(map(int, input().split()))
arr = []

for i in range(n) :
    temp = []
    s = input()
    for j in range(m) :
        temp.append(s[j])
    arr.append(temp)

def inRange(x, y) :
    return x >= 0 and y >= 0 and x < n and y < m

dxs, dys = [0, 0, 1, -1, -1, 1, 1, -1], [-1, 1, 0, 0, -1, 1, -1, 1]
cnt = 0

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 'L' :
            for dx, dy in zip(dxs, dys) :
                isLee = True
                for nn in range(1, 3) :
                    nx, ny = i + dx * nn, j + dy * nn
                    if not inRange(nx, ny) or arr[nx][ny] != 'E':
                        isLee = False
                        break

                if isLee :
                    cnt += 1


print(cnt)