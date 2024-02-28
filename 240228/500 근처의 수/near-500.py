import sys
arr = list(map(int, input().split()))

minVal, maxVal = sys.maxsize, -sys.maxsize

for elem in arr :
    if elem < 500 and elem > maxVal :
        maxVal = elem

    if elem > 500 and elem < minVal :
        minVal = elem

print(f"{maxVal} {minVal}")