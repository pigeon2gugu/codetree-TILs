arr = [list(input().split()) for _ in range(5)]

for i in range(len(arr)) :

    for j in range(len(arr[0])) :
        print(arr[i][j].upper(), end = " ")

    print()