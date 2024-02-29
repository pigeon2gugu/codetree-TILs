n = int(input())
arr = [[1 for _ in range(n)] for _ in range(n)]

for row in range(1, n) :
    for col in range(1, n) :
        arr[row][col] = arr[row-1][col] + arr[row][col-1] + arr[row-1][col-1]


for row in arr :
    for elem in row :
        print(elem, end = " ")
    print()