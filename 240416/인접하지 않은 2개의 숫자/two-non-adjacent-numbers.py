n = int(input())
nums = list(map(int, input().split()))

maxNum = 0
for i in range(n-2) :
    for j in range(i, n) :
        maxNum = max(maxNum, nums[i] + nums[j])

print(maxNum)