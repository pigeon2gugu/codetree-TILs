k, n = tuple(map(int, input().split()))

ranks = [
    list(map(int, input().split()))
    for _ in range(k)
]

ans = 0
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j :
            continue

        isTrue = True
        for kk in range(k) :
            for l in range(n) :

                if ranks[kk][l] == i :
                    aRank = l
                
                if ranks[kk][l] == j :
                    bRank = l

            
            if aRank > bRank :
                isTrue = False
                break
        
        if isTrue :
            ans += 1


print(ans)