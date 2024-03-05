a, b = tuple(input().split())

temp = a[:2]
arr = list(b)

arr[:2] = temp

answer = ''.join(arr)
print(answer)