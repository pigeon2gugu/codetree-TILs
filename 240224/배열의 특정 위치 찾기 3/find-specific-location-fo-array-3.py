arr = list(map(int, input().split()))
zeroIdx = arr.index(0)

print(arr[zeroIdx-1] + arr[zeroIdx-2] + arr[zeroIdx-3])