arrA = input().split()
arrB = input().split()
arrC = input().split()


aSym, aTemp = arrA[0], int(arrA[1])
bSym, bTemp = arrB[0], int(arrB[1])
cSym, cTemp = arrC[0], int(arrC[1])

cnt = 0

if aSym == 'Y' and aTemp >= 37 :
    cnt += 1

if bSym == 'Y' and bTemp >= 37 :
    cnt += 1

if cSym == 'Y' and cTemp >= 37 :
    cnt += 1

if cnt >= 2 :
    print("E")
else :
    print("N")