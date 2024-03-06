a = input()
b = input()

cnt = 0
while True :

    if a == b :
        break

    if cnt == len(a) :
        break

    a = a[-1] + a[:-1]
    cnt += 1

if cnt == len(a) :
    print(-1)
else :
    print(cnt)