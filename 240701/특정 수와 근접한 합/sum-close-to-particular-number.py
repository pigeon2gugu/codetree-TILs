import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

minSum = sys.maxsize

for i in range(n-3) :
    for j in range(i+1, n-2) :
        for k in range(j+1, n-1) :
            for l in range(k+1, n) :
                minSum = min(minSum, abs(s - (arr[i] + arr[j] + arr[k] + arr[l])))

print(minSum)