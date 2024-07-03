n, k = map(int, input().split())
candies = [0] * (400)
ans = 0

for _ in range(n) :
    count, point = map(int, input().split())
    candies[point] += count

for i in range(len(candies) - (2 * k)) :
    cnt = 0
    for j in range(i, i + 2 * k + 1) :
        cnt += candies[j]
    ans = max(ans, cnt)    

print(ans)