arr = list(map(int, input().split()))

a,b = arr[0], arr[1]
maxInt = b if b > a else a
print(maxInt)