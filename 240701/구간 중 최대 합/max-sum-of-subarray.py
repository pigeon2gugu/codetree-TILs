import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

maxSum = 0

for i in range(n - k + 1) :
    temp = 0
    for j in range(i, i + k) :
        temp += arr[j]
    
    maxSum = max(maxSum, temp)

print(maxSum)