

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    case = input().split()
    reversed_case = case[::-1]
    print(f"Case #{_ + 1}: {' '.join(reversed_case)}")