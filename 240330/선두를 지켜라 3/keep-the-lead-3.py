n, m = tuple(map(int, input().split()))
a = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]
maxL = 1000 * 1000 + 1
dA = [0] * (maxL)
dB = [0] * (maxL)

timeA = 1
for _, (v, t) in enumerate(a) :
    for _ in range(t) :
        dA[timeA] = dA[timeA - 1] + v
        timeA += 1

timeB = 1
for _, (v, t) in enumerate(b) :
    for _ in range(t) :
        dB[timeB] = dB[timeB - 1] + v
        timeB += 1

cnt = 0
for i in range(1, timeA - 1) :
    if (dA[i + 1] - dB[i + 1]) * (dA[i] - dB[i]) <= 0 :
        cnt += 1


print(cnt)