arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

if a < b :
    print(1, end = " ")
else :
    print(0, end = " ")

if a == b :
    print(1, end = " ")
else :
    print(0, end = " ")