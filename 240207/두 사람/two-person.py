arrA = input().split()
arrB = input().split()

aAge, aSex = int(arrA[0]), arrA[1]
bAge, bSex = int(arrB[0]), arrB[1]

if (aAge >= 19 and aSex == "M") or (bAge >= 19 and bSex == "M") :
    print(1)
else :
    print(0)