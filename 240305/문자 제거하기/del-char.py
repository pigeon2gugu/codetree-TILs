n = input()
arr = list(n)

while len(arr) > 1 :
    idx = int(input())

    if idx > len(arr) - 1 :
        idx = len(arr) - 1
        
    arr.pop(idx)
    print(''.join(arr))