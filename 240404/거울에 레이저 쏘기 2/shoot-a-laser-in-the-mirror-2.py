# \ : u -> l, l -> u, d -> r, r -> d
# / : d -> l, l -> d, u -> r, r -> u

n = int(input())
pattern = [input() for _ in range(n)]
arr = [list(row) for row in pattern]

start = int(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

def getStart(num):
    x, y = 0, 0
    
    if num // (n + 1) == 0:
        y = num % (n + 1) - 1
        x = 0
        direction = 0
    elif num // (n + 1) == 1:
        x = (num - n) % (n + 1) - 1
        y = n - 1
        direction = 1
    elif num // (n + 1) == 2:
        y = n - ((num - 2 * n) % (n + 1))
        x = n - 1
        direction = 2
    elif num // (n + 1) == 3:
        x = n - ((num - 3 * n) % (n + 1))
        y = 0
        direction = 3

    return (x, y, direction)

x, y, direction = getStart(start)

def inRange(x, y) :
    return x >= 0 and x < n and y >= 0 and y < n

ans = 0
while inRange(x, y) :
    ans += 1

    if arr[x][y] == '/' :
        if direction % 2 == 0 :
            direction = (direction + 1) % 4
        else :
            direction = (direction - 1) % 4
        
    elif arr[x][y] == '\\' :
        if direction % 2 == 0 :
            direction = (direction - 1) % 4
        else :
            direction = (direction + 1) % 4

    x = x + dxs[direction]
    y = y + dys[direction]

print(ans)