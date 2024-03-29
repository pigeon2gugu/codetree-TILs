maxL = 100000 + 1
n, m = tuple(map(int, input().split()))
a = [tuple(input().split()) for _ in range(n)]
b = [tuple(input().split()) for _ in range(m)]

disA = [0] * maxL
disB = [0] * maxL

timeA = 1
for _, (t, d) in enumerate(a) :
    for _ in range(int(t)) :
        if d == "L" :
            disA[timeA] = disA[timeA - 1] - 1
        elif d == "R" :
            disA[timeA] = disA[timeA - 1] + 1
        timeA += 1

timeB = 1
for _, (t, d) in enumerate(b) :
    for _ in range(int(t)) :
        if d == "L" :
            disB[timeB] = disB[timeB - 1] - 1
        elif d == "R" :
            disB[timeB] = disB[timeB - 1] + 1
        timeB += 1

maxT = max(timeA, timeB)

cnt = 0
for i in range(1, maxT) :
    dA = disA[i] if timeA > i else disA[timeA-1]
    dB = disB[i] if timeB > i else disB[timeB-1]

    dA1 = disA[i-1] if timeA > i - 1 else disA[timeA-1]
    dB1 = disB[i-1] if timeB > i - 1 else disB[timeB-1]
    
    if dA1 != dB1 and dA == dB :
        cnt += 1

print(cnt)