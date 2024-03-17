h1, m1, h2, m2 = tuple(map(int, input().split()))

t1 = 60 * h1 + m1
t2 = 60 * h2 + m2

print(t2 - t1)