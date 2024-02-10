arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

prod = 1
for i in range(a, b+1) :
    prod *= i

print(prod)