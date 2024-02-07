arr = list(map(int, input().split()))
a, b, c = arr[0], arr[1], arr[2]

max = a

if b >= a :
    if b > c:
        max =b
    else :
        max =c
elif c >= a :
    max = c
    
print(max)