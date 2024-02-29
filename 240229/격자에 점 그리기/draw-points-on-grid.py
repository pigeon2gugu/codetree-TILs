n, m = tuple(list(map(int, input().split())))
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m) :
    r, c = tuple(list(map(int, input().split())))
    arr[r-1][c-1] = i+1

for row in arr :
    for elem in row :
        print(elem, end = " ")
    print()