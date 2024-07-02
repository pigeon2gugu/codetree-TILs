n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n) :
    for j in range(i, n) :
        sumVal = 0
        for k in range(i, j+1) :
            sumVal += arr[k]
        
        avgVal = sumVal/(j+1-i)
        
        for k in range(i, j+1) :
            if avgVal == arr[k] :
                cnt += 1
                break


print(cnt)