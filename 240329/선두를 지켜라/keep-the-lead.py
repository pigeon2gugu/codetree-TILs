n, m = tuple(map(int, input().split()))
a = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]
maxT = 1000 * 1000 + 1

dA = [0] * maxT
dB = [0] * maxT

timeA = 0
for _, (v,t) in enumerate(a) :
    for _ in range(t) :
        timeA += 1
        dA[timeA] = dA[timeA-1] + v
        

timeB = 0
for _, (v,t) in enumerate(b) :
    for _ in range(t) :
        timeB += 1
        dB[timeB] = dB[timeB-1] + v


cnt = 0
for i in range(2, timeA) :

    if (dA[i] - dB[i]) != 0 and ((dA[i] - dB[i]) * (dA[i-1] - dB[i-1]) <= 0) :
        cnt += 1

print(cnt)