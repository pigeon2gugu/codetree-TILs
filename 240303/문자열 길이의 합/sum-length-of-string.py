n = int(input())
arr = [input() for _ in range(n)]

totalLength = 0
cnt = 0

for elem in arr :
    totalLength += len(elem)
    if elem[0] == "a" :
        cnt += 1

print(totalLength, cnt)