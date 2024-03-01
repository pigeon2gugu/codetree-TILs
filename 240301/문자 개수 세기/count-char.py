s1 = input()
s2 = input()

cnt = 0
for char in s1 :
    if s2 in char :
        cnt += 1

print(cnt)