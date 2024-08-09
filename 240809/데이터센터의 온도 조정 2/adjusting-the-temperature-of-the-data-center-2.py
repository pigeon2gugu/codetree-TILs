n, c, g, h = tuple(map(int, input().split()))

temp = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def getScore(temp, tempA, tempB) :
    if temp < tempA :
        return c
    
    elif temp >= tempA and temp <= tempB :
        return g

    return h

ans = 0
for t in range(1001) :
    score = 0
    for i in range(n) :
        score += getScore(t, temp[i][0], temp[i][1])

    ans = max(ans, score)

print(ans)