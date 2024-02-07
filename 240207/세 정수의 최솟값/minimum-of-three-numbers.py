arr = list(map(int, input().split()))
a, b, c = arr[0], arr[1], arr[2]

min = a

if b < a and b <= c:
    min = b

if c < a and c <= b :
    min = c

print(min)