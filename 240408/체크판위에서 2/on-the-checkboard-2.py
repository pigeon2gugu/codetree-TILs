r, c = tuple(map(int, input().split()))
arr = [list(input().split()) for _ in range(r)]
answer = []

cnt = 0
start = arr[0][0]
end = arr[-1][-1]

for i in range(1, r-1) :
    for j in range(1, c-1) :
        if arr[i][j] != start :
            for k in range(i+1, r - 1) :
                for l in range(j+1, c - 1) :
                    if arr[k][l] != end and arr[k][l] != arr[i][j] :
                        cnt+=1

print(cnt)