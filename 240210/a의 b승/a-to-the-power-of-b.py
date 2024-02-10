arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

prod = 1

for _ in range(b) :
    prod *= a

print(prod)