n = int(input())
arr = [input() for _ in range(n)]
s = input()

totalLength = 0
cnt = 0

for elem in arr :
    if elem[0] == s :
        totalLength += len(elem)
        cnt += 1

print(f"{cnt} {(totalLength/cnt):.2f}")