lenArr = int(input())
arr = list(map(int, input().split()))

cnt = 0
idx = -1

for i,elem in enumerate(arr) :
    if elem == 2 :
        idx = i + 1
        cnt += 1

    if cnt == 3 :
        print(idx)
        break