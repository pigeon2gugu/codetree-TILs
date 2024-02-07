arrA = input().split()
arrB = input().split()

aAge, aSex = int(arrA[0]), arrA[1]
bAge, bSex = int(arrB[0]), arrB[1]

if aAge < 19 and bAge < 19 and aSex == "W" and bSex == "W" :
    print(0)
else :
    print(1)