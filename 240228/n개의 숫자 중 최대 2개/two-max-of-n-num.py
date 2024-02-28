n = int(input())
arr = list(map(int, input().split()))

maxVal = max(arr)
maxValIdx = arr.index(max(arr))

maxVal2 = sys.minsize
for i, elem in enumerate(arr) :
    if i == maxValIdx :
        continue

    if elem > maxVal2 :
        maxVal2 = elem

print(f"{maxVal} {maxVal2}")