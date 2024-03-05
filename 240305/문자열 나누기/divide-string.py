n = int(input())
arr = input().split()

s = ''.join(arr)

temp = ""
cnt = 0
for c in s :
    temp += c
    cnt += 1
    if cnt == 5 :
        print(temp)
        temp = ""
        cnt = 0

print(temp)