n = int(input())

cnt = 0
nn = n
for i in range(1, n+1) :
    cnt += 1
    nn = nn // i
    if nn <= 1 :
        print(cnt)
        break