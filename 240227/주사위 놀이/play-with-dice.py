arr = list(map(int, input().split()))
cntArr = [0 for _ in range(6)]

for elem in arr :
    cntArr[elem - 1] += 1

for i in range(len(cntArr)) :
    print(f"{i+1} - {cntArr[i]}")