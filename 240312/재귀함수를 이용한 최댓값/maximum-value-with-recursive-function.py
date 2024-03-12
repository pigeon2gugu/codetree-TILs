n = int(input())
arr = list(map(int, input().split()))

maxVal = arr[-1]

def getMax(idx) :
    global maxVal
    if idx == 0 :
        return maxVal

    if maxVal < arr[idx-1] :
        maxVal = arr[idx-1]
    
    return getMax(idx-1)


print(getMax(len(arr)))