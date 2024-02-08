arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

while a <= b :
    print(a, end = " ")
    if a%2 == 1 :
        a *= 2
    else :
        a += 3