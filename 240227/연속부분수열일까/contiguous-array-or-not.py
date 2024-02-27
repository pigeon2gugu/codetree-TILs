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
            if idx + 1 > len(arrA) - 1 :
                tf = "No"
                break 

            if arrA[idx+1] != elemB :
                tf = "No"
                break

            tf = "Yes"
        
        if tf == "Yes" :
            break

print(tf)