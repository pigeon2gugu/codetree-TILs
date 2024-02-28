n = int(input())
arr = list(map(int, input().split()))

maxVal = 0

for i in range(len(arr)-1) :
    if max(arr[i::]) - arr[i] > maxVal :
        maxVal = max(arr[i::]) - arr[i]

print(maxVal)