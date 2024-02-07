arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

aMath, aEng = arrA[0], arrA[1]
bMath, bEng = arrB[0], arrB[1]

if aMath == bMath and aEng > bEng :
    print("A")
elif aMath == bMath and aEng < bEng :
    print("B")
elif aMath > bMath :
    print("A")
else :
    print("B")