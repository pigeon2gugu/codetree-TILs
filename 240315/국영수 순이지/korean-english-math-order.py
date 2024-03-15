n = int(input())

inputs = [input().split() for _ in range(n)]
students = [(name, int(kor), int(eng), int(math)) for name, kor, eng, math in inputs]

students.sort(key = lambda x : (-x[1], -x[2], -x[3]))

for s in students :
    print(f"{s[0]} {s[1]} {s[2]} {s[3]}")