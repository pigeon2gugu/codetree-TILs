arr = list(map(int, input().split()))

a, b, c = arr[0], arr[1], arr[2]

if a >= b :
    if c > a :
        print(a)
    elif c > b:
        print(c)
    else :
        print(b)
else :
    if c > b :
        print(b)
    elif c > a:
        print(c)
    else :
        print(a)