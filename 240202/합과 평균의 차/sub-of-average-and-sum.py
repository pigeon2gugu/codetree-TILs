arr = list(map(int, input().split()))
a = sum(arr)
b = sum(arr)//len(arr)
c = a-b

print(a, b, c, sep = "\n")