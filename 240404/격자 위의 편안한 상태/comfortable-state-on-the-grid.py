n, m = tuple(map(int, input().split()))
arr = [[0] * (n + 1) for _ in range(n+1)]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def isRange(x, y) :
    return x > 0 and x <= n and y > 0 and y <= n  

def isStable(x, y) :

    cnt = 0
    for i in range(4) :
        if isRange(x+dxs[i], y+dys[i]) and arr[x + dxs[i]][y + dys[i]] == 1 :
            cnt += 1

    if cnt == 3 :
        return True

    return False


for i in range(m) :
    x, y = tuple(map(int, input().split()))
    x, y = x, y

    arr[x][y] = 1

    if isStable(x, y) :
        print(1)
    else :
        print(0)