n = int(input())
nums = [int(input()) for _ in range(n)]

cnts = []
cnt = 1
for i in range(1, n) :
    if nums[i-1] == nums[i] :
        cnt += 1
    else :
        cnts.append(cnt)
        cnt = 1

cnts.append(cnt)
print(max(cnts))