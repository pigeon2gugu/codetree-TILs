n, k, p, t = tuple(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(t)]
attacked = [0] * (n + 1)
attacked[p] = 1

arr.sort(key = lambda x : x[0])

cnt = 0
for _ , (time, x, y) in enumerate(arr) :

    if x == p or y == p :
        cnt += 1

        if cnt > k :
            break

        attacked[x] = 1
        attacked[y] = 1


for a in attacked[1::] :
    print(a, end = "")