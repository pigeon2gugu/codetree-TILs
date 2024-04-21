n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

def isNotOverlap(x1, y1, x2, y2) :

    if x1 == x2 :
        return y2 - y1 > 2 and inRange(x2, y2)

    return inRange(x2, y2)

maxCnt = 0
for i in range(n) :
    for j in range(1, n-1) :
        for k in range(n) :
            for l in range(1, n-1) :
                cnt = 0
                if isNotOverlap(i, j, k, l) :  
                    for m in range(-1, 2) :
                        if arr[i][j+m] == 1 :
                            cnt = cnt + 1
                        if arr[k][l+m] == 1 :
                            cnt = cnt + 1

                maxCnt = max(cnt, maxCnt)

print(maxCnt)