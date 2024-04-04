stmts = input()

x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

direction = 0
cnt = 0
isZero = False

for stmt in stmts :

    cnt += 1

    if stmt == 'R' :
        direction = (direction + 1) % 4
    elif stmt == 'L' :
        direction = (direction + 3) % 4
    elif stmt == 'F' :
        x = x + dxs[direction]
        y = y + dys[direction]

    if x == 0 and y == 0 :
        isZero = True
        break

    

if not isZero :
    print(-1)
else :
    print(cnt)