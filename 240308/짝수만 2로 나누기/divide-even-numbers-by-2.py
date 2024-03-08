n = int(input())
arr = list(map(int, input().split()))

def div2(arr) :
    for i in range(len(arr)) :
        if arr[i] % 2 == 0 :
            arr[i] = arr[i]//2


div2(arr)

for elem in arr :
    print(elem, end = " ")