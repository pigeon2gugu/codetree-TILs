arr = list(map(int, input().split()))

notZeroArr = []
for i in range(len(arr)) :
    if i != 0 :
        notZeroArr.append(arr[i])

sumVal = sum(notZeroArr)
avg = sumVal/len(notZeroArr)

print(sumVal, end = " ")
print(f"{avg:.1f}")