n = int(input())
arr = list(map(int, input().split()))

arr.sort()

for elem in arr :
    print(elem, end = " ")

print()

reversedArr = list(reversed(arr))

for elem in reversedArr :
    print(elem, end = " ")