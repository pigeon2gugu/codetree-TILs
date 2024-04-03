n = int(input())
stmts = [tuple(input().split()) for _ in range(n)]

directions = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
dx, dy = [0, 1, 0, -1] , [-1, 0, 1, 0]

cnt = 0
x, y = 0, 0
isArrived = False

for s in stmts :

    if isArrived :
        break

    direction = directions[s[0]]
    distance = int(s[1])

    for d in range(distance) :
        cnt += 1
        x = x + dx[direction]
        y = y + dy[direction]

        if x == 0 and y == 0 :
            isArrived = True
            break


if not isArrived :
    print(-1)
else :
    print(cnt)