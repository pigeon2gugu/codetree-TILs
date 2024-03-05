s = input()
arr = list(s)

arr[1] = 'a'
arr[-2] = 'a'

answer = ''.join(arr)

print(answer)