n, A = tuple(input().split())
n = int(n)

cnt = 0
for _ in range(n) :
    s = input()
    if s == A :
        cnt += 1

print(cnt)