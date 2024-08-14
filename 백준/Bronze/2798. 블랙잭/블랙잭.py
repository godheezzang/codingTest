# import sys
# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
cards = list(map(int, input().split()))
first_used = [False] * n
second_used = [False] * n
third_used = [False] * n
ret = 0
totals = []
abs_min = 21e8
for i in range(n):
    first_used[i] = True
    first = cards[i]
    for j in range(n):
        if first_used[j] == True: continue
        second_used[j] = True
        second = cards[j]
        for k in range(j+1, n):
            if second_used[k] == True or first_used[k] == True: continue
            third = cards[k]
            third_used[k] = True
            total = first + second + third
            totals.append(total)
            third_used[k] = False
        second_used[j] = False
    first_used[i] = False
for i in range(len(totals)):
    if totals[i] <= m:
        if abs(totals[i] - m) < abs_min:
            abs_min = abs(totals[i]-m)
            ret = totals[i]
print(ret)