arr = list(map(int, input().split()))
b, a = arr[0], arr[1]

for i in range(b, a-1, -1) :
    if i%2 == 1 :
        print(i, end = " ")