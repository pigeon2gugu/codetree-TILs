arr = list(map(int, input().split()))

notZeroArr = []
for i in range(len(arr)) :
    if arr[i] == 0 :
        break

    notZeroArr.append(arr[i])
        

sumVal = sum(notZeroArr)
avg = sumVal/len(notZeroArr)

print(sumVal, end = " ")
print(f"{avg:.1f}")