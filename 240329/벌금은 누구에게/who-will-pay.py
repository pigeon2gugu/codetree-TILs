n, m, k = tuple(map(int, input().split()))
panalties = [0] * (n+1)

cnt = 0
for _ in range(m) :
    idx = int(input())
    panalties[idx] += 1

    if panalties[idx] >= k :
        print(idx)
        cnt += 1
        break

if cnt == 0 :
    print(-1)