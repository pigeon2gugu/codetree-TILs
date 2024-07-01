n, k = map(int, input().split())
pictures = [0] * 10001

maxSum = 0

for _ in range(n) :
    info = input().split()
    point = int(info[0])
    alpha = info[1]

    if alpha == 'G' :
        pictures[point] = 1
    elif alpha == 'H' :
        pictures[point] = 2



for i in range(len(pictures) - k) :
    temp = 0
    for j in range(i, i + k + 1) :
        temp += pictures[j]

    maxSum = max(maxSum, temp)

print(maxSum)