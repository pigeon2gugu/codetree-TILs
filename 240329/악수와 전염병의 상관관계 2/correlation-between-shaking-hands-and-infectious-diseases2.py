n, k, p, t = tuple(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(t)]
attacked = [0] * (n + 1)
cnts = [0] * (n + 1)

attacked[p] = 1

arr.sort(key = lambda x : x[0])


for _ , (time, x, y) in enumerate(arr) :

    if attacked[x] == 1 and cnts[x] < k :
        cnts[x] += 1
        attacked[y] = 1

    if attacked[y] == 1 and cnts[y] < k and cnts[y] > 0:
        cnts[y] += 1
        attacked[x] = 1


for a in attacked[1::] :
    print(a, end = "")