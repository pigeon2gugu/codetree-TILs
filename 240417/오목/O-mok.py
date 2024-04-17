s = [list(map(int, input().split())) for _ in range(19)]
length = 19

winner = 0
x = 0
y = 0
hasWinner = False
for i in range(length) :
    for j in range(length) :

        if s[i][j] == 0 :
            continue

        color = s[i][j]
        if s[i-2][j] == color and s[i-1][j] == color and s[i+1][j] == color and s[i+2][j] == color :
            hasWinner = True
            break
        elif s[i][j-2] == color and s[i][j-1] == color and s[i][j+1] == color and s[i][j+2] == color :
            hasWinner = True
            break
        elif s[i-2][j-2] == color and s[i-1][j-1] == color and s[i+1][j+1] == color and s[i+2][j+2] == color :
            hasWinner = True
            break
        elif s[i-2][j+2] == color and s[i-1][j+1] == color and s[i+1][j-1] == color and s[i+2][j-2] == color :
            hasWinner = True
            break
            

    if hasWinner :
        winner = color
        x = i + 1
        y = j + 1
        break

        
if hasWinner :
    print(winner)
    print(x, y)
else :
    print(0)