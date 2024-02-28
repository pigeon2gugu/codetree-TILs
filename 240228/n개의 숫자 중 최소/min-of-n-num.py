n = int(input())
arr = list(map(int, input().split()))

minVal = min(arr)
cnt = 0

for elem in arr :
    if elem == minVal :
        cnt += 1

print(f"{minVal} {cnt}")