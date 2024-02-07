arr = list(map(int, input().split()))
a, b= arr[0], arr[1]

for i in range(a, b+1) :
    if i%2 == 1:
        print(i, end = " ")