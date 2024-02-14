arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

isTrue = False
for i in range(a, b+1) :
    if 1920 % i == 0 and 2880 % i == 0 :
        isTrue = True
        break

print(int(isTrue))