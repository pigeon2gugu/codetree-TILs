m1, d1, m2, d2 = tuple(map(int, input().split()))

dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1Date = sum(dayOfMonth[:m1]) + d1
m2Date = sum(dayOfMonth[:m2]) + d2

print(m2Date - m1Date)