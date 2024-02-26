n = int(input())
arr = []

idx = 1
cnt = 0

while True :
    arr.append(n * idx)
    
    if (n * idx) % 5 == 0 :
        cnt += 1

    if cnt == 2 :
        for elem in arr :
            print(elem, end = " ")
        break

    idx += 1