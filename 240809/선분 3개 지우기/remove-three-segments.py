from itertools import combinations

n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def is_non_overlapping(segments):
    segments.sort()
    for i in range(len(segments) - 1):
        if segments[i][1] >= segments[i + 1][0]:
            return False
    return True

def count_valid_combinations(n, segments):
    valid_combinations = 0
    all_combinations = combinations(segments, n - 3)
    
    for combination in all_combinations:
        if is_non_overlapping(list(combination)):
            valid_combinations += 1
    
    return valid_combinations

print(count_valid_combinations(n, segments))