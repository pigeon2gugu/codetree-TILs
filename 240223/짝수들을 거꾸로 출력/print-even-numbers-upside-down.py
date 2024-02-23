n = int(input())
arr = list(map(int, input().split()))
rvsArr = arr[::-1]

for elem in rvsArr :
    if elem % 2 == 0:
        print(elem, end = " ")