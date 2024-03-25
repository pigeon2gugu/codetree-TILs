n = int(input())
stmts = [tuple(input().split()) for _ in range(n)]
maxL = n * 100 * 2

colors = [0] * (maxL + 1)

start = maxL // 2
for s in stmts :
    if s[1] == "L" :
        for i in range(start - int(s[0]) + 1, start + 1) :
            colors[i] = 1
        start = start - int(s[0]) + 1

    elif s[1] == "R" :
        for i in range(start, start + int(s[0])) :
            colors[i] = 2
        start = start + int(s[0]) - 1

cntW = 0
cntB = 0

for c in colors :
    if c == 1 :
        cntW += 1
    elif c == 2 :
        cntB += 1

print(cntW, cntB)