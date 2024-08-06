from itertools import combinations

n, b = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]
ans = 0

for r in range(1, n + 1):
    for combo in combinations(range(n), r):
        total_price = sum(arr[i] for i in combo)
            
        for i in combo:
            discounted_price = total_price - arr[i] // 2
            if discounted_price <= b:
                ans = max(ans, r)
                break

print(ans)