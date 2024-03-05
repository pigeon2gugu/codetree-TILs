n = input()
f = n[0]
s = n[1]

arr = list(n)

for i in range(len(arr)) :
    if arr[i] == s :
        arr[i] = f

answer = ''.join(arr)
print(answer)