n = int(input())
arr = list(map(int, input().split()))

newArr = [elem ** 2 for elem in arr]

for elem in newArr :
    print(elem, end = " ")