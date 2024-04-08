import sys
n = int(input())
arr = list(map(int, input().split()))

minD = sys.maxsize
for i in range(len(arr)) :
    distance = 0
    for j in range(len(arr)) :
         distance += abs(j-i) * arr[j]
    
    minD = min(minD, distance)

print(minD)