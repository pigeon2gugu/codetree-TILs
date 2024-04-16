n = int(input())
nums = [input() for _ in range(n)]

maxNum = 0
for i in range(len(nums) - 2) :

    temp = int(nums[i])
    cnt = 0

    for j in range(i + 1, len(nums) - 1) :
        isCarry = False
        
        for k in range(min(len(str(temp)), len(nums[j]))) :
            if int(str(temp)[len(str(temp)) - k - 1]) + int(nums[j][len(nums[j]) - k - 1]) > 9 :
                isCarry = True
                break
        
        if not isCarry :
            temp += int(nums[j])
            for k in range(j + 1, len(nums)) :
                isCarry = False
                for l in range(min(len(str(temp)), len(nums[k]))) :
                    if int(str(temp)[len(str(temp)) - l - 1]) + int(nums[k][len(nums[k]) - l - 1]) > 9 :
                        isCarry = True
                        break

                if not isCarry :
                    maxNum = max(temp + int(nums[k]), maxNum)


if maxNum == 0 :
    print(-1)
else :
    print(maxNum)