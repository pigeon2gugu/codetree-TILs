n = int(input())
dx = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
dy = {'N': 1, 'E': 0, 'S': -1, 'W': 0}

x, y = 0, 0

for _ in range(n):
    direction, move = input().split()
    x += dx[direction] * int(move)
    y += dy[direction] * int(move)

print(x, y)