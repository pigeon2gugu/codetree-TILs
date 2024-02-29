n = 5

arr = [[1 for _ in range(5)] for _ in range(5)]

for row in range(5) :
    arr[row][0] = 1

for row in range(1, 5) :
    for col in range(1, 5) :
        arr[row][col] = arr[row][col-1] + arr[row-1][col]

for row in arr :
    for elem in row :
        print(elem, end = " ")
    print()