import sys
n = int(input())
arr = list(map(int, input().split()))

minVal = sys.maxsize

for i, elem in enumerate(arr[:len(arr)-1]) :

    for elems in arr[i+1::] :
        temp = abs(elem - elems)

        if temp < minVal :
            minVal = temp

print(minVal)