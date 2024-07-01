import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        remaining_sum = sum(arr) - arr[i] - arr[j]
        current_diff = abs(s - remaining_sum)
        min_diff = min(min_diff, current_diff)

print(min_diff)