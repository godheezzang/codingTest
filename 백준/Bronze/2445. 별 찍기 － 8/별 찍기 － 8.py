# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

n = int(input(""))

def solve(n):
    for i in range(1, n + 1):
        print("*" * i + " " * 2 * (n - i) + "*" * i)
    for i in range(1, n):
        print("*" * (n - i) + " " * 2 * i + "*" * (n - i))

solve(n)