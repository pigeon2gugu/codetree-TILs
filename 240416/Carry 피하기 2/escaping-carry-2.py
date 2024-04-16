n = int(input())
nums = [input() for _ in range(n)]

maxNum = 0
for i in range(len(nums) - 2) :
    for j in range(i + 1, len(nums) - 1) :
        for k in range(j + 1, len(nums)) :
            maxL = max(len(nums[i]), len(nums[j]), len(nums[k]))
            tempMax = str(max(int(nums[i]), int(nums[j]), int(nums[k])))
            isCarry = False

            if len(nums[i]) < maxL :
                nums[i] = '0' * (maxL - len(nums[i])) + nums[i]

            if len(nums[j]) < maxL :
                nums[j] = '0' * (maxL - len(nums[j])) + nums[j]
            
            if len(nums[k]) < maxL :
                nums[k] = '0' * (maxL - len(nums[k])) + nums[k]

            for l in range(maxL) :
                if int(nums[i][l]) + int(nums[j][l]) + int(nums[k][l]) > 9 :
                    isCarry = True
                    break

            if not isCarry :
                maxNum = max(maxNum, int(nums[i]) + int(nums[j]) + int(nums[k]))


if maxNum == 0 :
    print(-1)
else :
    print(maxNum)