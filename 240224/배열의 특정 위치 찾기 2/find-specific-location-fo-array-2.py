arr = list(map(int, input().split()))

sum1 = sum(arr[::2])
sum2 = sum(arr[1::2])

if sum1 > sum2 :
    print(sum1 - sum2)
else :
    print(sum2 - sum1)