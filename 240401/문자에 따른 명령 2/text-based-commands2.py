l = input()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
direction = 3

for ll in l :
    if ll == 'R' :
        direction += 1
    elif ll == 'L' :
        direction = direction -1 + 4
    elif ll == 'F' :
        x += dx[direction % 4]
        y += dy[direction % 4]


print(x, y)