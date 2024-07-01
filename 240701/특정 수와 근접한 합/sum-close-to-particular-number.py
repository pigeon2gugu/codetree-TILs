import sys
sys.setrecursionlimit(100000)

n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = sys.maxsize

def find_min_diff(arr, n, s, selected, start):
    global min_diff
    if len(selected) == n-2:
        current_sum = sum(selected)
        current_diff = abs(s - current_sum)
        min_diff = min(min_diff, current_diff)
        return

    for i in range(start, len(arr)):
        find_min_diff(arr, n, s, selected + [arr[i]], i + 1)

find_min_diff(arr, n, s, [], 0)

print(min_diff)