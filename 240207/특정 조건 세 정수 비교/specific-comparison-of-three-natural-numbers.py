arr = list(map(int, input().split()))
a, b, c, = arr[0], arr[1], arr[2]

print(int(a==min(arr)), end = " ")
print(int(a==b==c))