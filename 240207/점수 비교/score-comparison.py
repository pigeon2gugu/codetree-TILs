math = list(map(int, input().split()))
eng = list(map(int, input().split()))

aMath, bMath = math[0], math[1]
aEng, bEng = eng[0], eng[1]

if aMath >= bMath and aEng >= bEng :
    print(1)
else :
    print(0)