n = int(input())
stmts = [tuple(input().split()) for _ in range(n)]
maxL = n * 100 * 2

colors = [0] * (maxL + 1)
cntW = [0] * (maxL + 1)
cntB = [0] * (maxL + 1)

start = n * 100

for s in stmts :
    if s[1] == "R" :
        for i in range(start, start + int(s[0])) :
            colors[i] = 1
            cntB[i] += 1
        start = start + int(s[0]) - 1
    
    elif s[1] == "L" :
        for i in range(start - int(s[0]) + 1, start + 1) :
            colors[i] = -1
            cntW[i] += 1
        start = start - int(s[0]) + 1


cnt1, cnt2, cnt3 = 0, 0, 0

for i in range(len(colors)) :
    if cntW[i] >= 2 and cntB[i] >= 2 :
        cnt3 += 1
    else :
        if colors[i] == -1 :
            cnt1 += 1
        elif colors[i] == 1 :
            cnt2 += 1


print(cnt1, cnt2, cnt3)