import sys

n = int(input())
arr = list(map(int, input().split()))
answer = []
maxVal = max(arr)
maxIdx = arr.index(maxVal) + 1
answer.append(maxIdx)

while True :

    if maxIdx == 1 :
        break

    maxVal = max(arr[:maxIdx-1])
    maxIdx = arr.index(maxVal) + 1
    answer.append(maxIdx)
    
for elem in answer :
    print(elem, end = " ")