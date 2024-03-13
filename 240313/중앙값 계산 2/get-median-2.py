n = int(input())
arr = list(map(int, input().split()))

answer = []
for i in range(len(arr)) :
    if i % 2 == 0 :
        sArr = sorted(arr[:i+1])
        answer.append(sArr[(i+1)//2])


for elem in answer :
    print(elem, end = " ")