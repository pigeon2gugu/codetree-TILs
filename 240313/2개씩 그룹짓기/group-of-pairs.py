n = int(input())
arr = list(map(int, input().split()))

arr.sort()
sumArr = []

for i in range(n) :
    sumArr.append(arr[i] + arr[len(arr) - i -1])

print(max(sumArr))