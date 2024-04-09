n = input()
arr = [int(nn) for nn in n]

maxNum = 0
for i in range(len(arr)) :
    temp = arr[i]
    num = 0
    if arr[i] == 0 :
        arr[i] = 1
    else :
        arr[i] = 0

    for idx, a in enumerate(arr) :
        num += a * (2 **(len(arr) - idx -1))

    maxNum = max(maxNum, num)
    arr[i] = temp
        
print(maxNum)