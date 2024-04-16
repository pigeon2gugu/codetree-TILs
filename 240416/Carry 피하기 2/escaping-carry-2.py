n = int(input())
nums = [input() for _ in range(n)]

maxNum = 0
for i in range(len(nums) - 1) :

    temp = int(nums[i])
    cnt = 0

    for j in range(i + 1, len(nums)) :
        isCarry = False
        
        for k in range(min(len(str(temp)), len(nums[j]))) :
            if int(str(temp)[len(str(temp)) - k - 1]) + int(nums[j][len(nums[j]) - k - 1]) > 9 :
                isCarry = True
                break
        
        if not isCarry : 
            temp += int(nums[j])
            cnt += 1

    if cnt == 2 :
        maxNum = max(maxNum, temp)

if maxNum == 0 :
    print(-1)
else :
    print(maxNum)