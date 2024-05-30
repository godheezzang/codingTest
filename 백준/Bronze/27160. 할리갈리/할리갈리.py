# x, y

import random
def solve():
    n = int(input())
    cards = {
        'STRAWBERRY': 0,
        'BANANA': 0,
        'LIME': 0,
        'PLUM': 0
    }
    for i in range(n):
        s, x = input().split()
        cards[s] += int(x)

    bell = 5 in cards.values()
    if bell: print('YES')
    else: print('NO')

solve()
