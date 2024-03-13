n, k, t = tuple(input().split())
n = int(n)
k = int(k)

tArr = []

for _ in range(n) :
    s = input()
    if s[:len(t)] == t :
        tArr.append(s)


tArr.sort()

print(tArr[k-1])