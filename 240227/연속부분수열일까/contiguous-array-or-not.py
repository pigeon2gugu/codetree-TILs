lenA, lenB = tuple(map(int, input().split()))
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))


firstIdx = []
tf = "Yes"

for i, elem in enumerate(arrA) :
    if elem == arrB[0] :
        firstIdx.append(i)

if len(firstIdx) == 0 :
    tf = "No"
else :
    for elem in firstIdx :
        idx = elem

        for elemB in arrB :
            if idx + 1 > len(arrA) :
                tf = "No"
                break 

            if arrA[idx] != elemB :
                tf = "No"
                break

            idx += 1
            tf = "Yes"
        
        if tf == "Yes" :
            break

print(tf)