n, m = tuple(list(map(int, input().split())))
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

answer = [[1 for _ in range(m)] for _ in range(n)]

for i in range(len(arr1)) :
    for j in range(len(arr1[0])) :
        if arr1[i][j] == arr2[i][j] :
            answer[i][j] = 0


for row in answer :
    for elem in row :
        print(elem, end = " ")
    print()