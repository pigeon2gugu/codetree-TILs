n, m = tuple(map(int, input().split()))
a = [tuple(input().split()) for _ in range(n)]
b = [tuple(input().split()) for _ in range(m)]
maxT = 1000 * 1000 + 1
arrA = [0] * maxT
arrB = [0] * maxT

timeA = 0
for i in range(len(a)) :
    t = int(a[i][1])
    for tt in range(t) :
        if a[i][0] == "L" :
            arrA[timeA+1] = arrA[timeA] - 1
        elif a[i][0] == "R" :
            arrA[timeA+1] = arrA[timeA] + 1
        timeA += 1

timeB = 0
for i in range(len(b)) :
    t = int(b[i][1])
    for tt in range(t) :
        if b[i][0] == "L" :
            arrB[timeB+1] = arrB[timeB] - 1
        elif b[i][0] == "R" :
            arrB[timeB+1] = arrB[timeB] + 1
        timeB += 1

maxTime = max(timeA, timeB)

ans = -1
for i in range(1, maxTime) :
    if arrA[i] == arrB[i] :
        ans = i
        break

print(ans)