n = int(input())
nums = [int(input()) for _ in range(n)]

cnts = []
cnt = 0
for i in range(n) :
    if i == 0 or nums[i-1] == nums[i] :
        cnt += 1
    else :
        cnts.append(cnt)
        cnt = 1


print(max(cnts))