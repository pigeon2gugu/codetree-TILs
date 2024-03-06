n = int(input())

def printSquare(num) :
    cnt = 1
    for _ in range(num) :
        for _ in range(num) :

            if cnt == 10 :
                cnt = 1

            print(cnt, end = " ")
            cnt += 1
        print()


printSquare(n)