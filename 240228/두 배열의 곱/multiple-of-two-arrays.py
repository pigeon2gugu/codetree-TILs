arrA = [list(map(int, input().split())) for _ in range(3)]
input().split()
arrB = [list(map(int, input().split())) for _ in range(3)]


for i in range(len(arrA)) :
    for j in range(len(arrA[0])) :
        print(arrA[i][j] * arrB[i][j], end = " ")
    print()