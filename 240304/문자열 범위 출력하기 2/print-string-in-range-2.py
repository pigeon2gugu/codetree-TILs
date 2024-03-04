s = input()
n = int(input())

cnt = 0
while True :
    if cnt >= len(s) or cnt >= n :
        break
    print(s[len(s)-1-cnt], end = "")
    cnt += 1