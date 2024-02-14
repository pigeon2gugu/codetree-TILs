arr = list(map(int, input().split()))
a, b, c = arr[0], arr[1], arr[2]

isTrue = True
for i in range(a, b+1) :
    if i % c == 0 :
        isTrue = False
        break

if isTrue :
    print("YES")
else :
    print("NO")