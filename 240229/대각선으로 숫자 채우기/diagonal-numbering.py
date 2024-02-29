n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

num = 1
for i in range(m):
    arr[0][i] = num
    num += 1

    temp = 1
    while temp < len(arr) and i - temp >= 0:
        arr[temp][i - temp] = num
        num += 1
        temp += 1

while num <= n * m:
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 0:
                arr[row][col] = num
                num += 1

                temp = 1
                while row + temp < n and col - temp >= 0:
                    arr[row + temp][col - temp] = num
                    num += 1
                    temp += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()