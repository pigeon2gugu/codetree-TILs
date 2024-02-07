arr = list(map(int, input().split()))
m, l = arr[0], arr[1]

if m < 90 :
    print(0)
elif l >= 95 :
    print(100000)
elif l >= 90 :
    print(50000)
else :
    print(0)