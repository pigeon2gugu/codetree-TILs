n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = 0

def isNear(a, b) :
    if (abs(a - b) <= 2 or abs(a - b) >= n - 2) :
        return True
    
    return False


def isOpen(i, j, k) :
    if isNear(arr1[0], i) and isNear(arr1[1], j) and isNear(arr1[2], k) :
        return True
    
    if isNear(arr2[0], i) and isNear(arr2[1], j) and isNear(arr2[2], k) :
        return True

    return False


for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        for k in range(1, n + 1) :
            if isOpen(i, j, k) :
                ans += 1

print(ans)