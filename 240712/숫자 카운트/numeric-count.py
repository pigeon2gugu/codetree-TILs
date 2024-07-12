n = int(input())
queries = []
numbers = []
ans = 0

for _ in range(n):
    query, count1, count2 = input().split()
    queries.append((query, int(count1), int(count2)))

for i in range(1, 10) :
    for j in range(1, 10) :
        for k in range(1, 10) :
            number = i * 100 + j * 10 + k
            numbers.append(str(number))

def calculateCounts(a, b):
    count1 = sum(1 for i in range(3) if a[i] == b[i])
    count2 = sum(1 for i in range(3) if a[i] != b[i] and a[i] in b)
    return count1, count2

for number in numbers:
    valid = True
    for query, count1, count2 in queries:
        calculatedCount1, calculatedCount2 = calculateCounts(number, query)

        if count1 != calculatedCount1 or count2 != calculatedCount2:
            valid = False
            break

    if valid:
        ans += 1
    
print(ans)