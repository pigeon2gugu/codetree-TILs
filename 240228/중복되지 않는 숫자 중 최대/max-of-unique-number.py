n = int(input())
arr = list(map(int, input().split()))
newArr = set(arr)
answerArr = []

for elem in newArr :
    cnt = 0

    for elem2 in arr :
        if elem2 == elem :
            cnt += 1

    if cnt == 1 :
        answerArr.append(elem)

if len(answerArr) == 0 :
    print(-1)
else :
    print(max(answerArr))