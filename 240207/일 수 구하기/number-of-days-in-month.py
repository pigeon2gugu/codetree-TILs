n = int(input())

if n <= 7 :
    if n%2 == 0 and n != 2 :
        print(30)
    elif n%2 == 1 :
        print(31)
    else :
        print(28)
else :
    if n%2 == 0 :
        print(31)
    elif n%2 == 1 :
        print(30)