def solve():
    result = ""
    word = input().split("-")
    for short in word:
        result += short[0]
    print(result.upper())
solve()