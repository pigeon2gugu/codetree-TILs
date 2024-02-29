n = int(input())
arr = [[1 for _ in range(n)] for _ in range(n)]

for row in range(n) :

    for col in range(1, row) :
        arr[row][col] = arr[row-1][col-1] + arr[row-1][col]


for row in range(n) :
    for col in range(n) :
        if col > row :
            continue
        print(arr[row][col], end = " ")
    print()