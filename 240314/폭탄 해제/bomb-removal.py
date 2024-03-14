a, b, c = tuple(input().split())
c = int(c)

class Bomb :
    def __init__(self, code, color, time) :
        self.code = code
        self.color = color
        self.time = time


bomb = Bomb(a, b, c)

print(f"code : {bomb.code}")
print(f"color : {bomb.color}")
print(f"second : {bomb.time}")