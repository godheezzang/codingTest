n, k = map(int, input().split())
coins = []
inf = int(21e8)
arr = [inf] * (k+1)
arr[0] = 0
for i in range(n):
    value = int(input())
    coins.append(value)

coins.sort()

for i in range(n):
    start = coins[i]
    for j in range(start, k+1):
        arr[j] = min(arr[j], arr[j-start]+1)

if arr[k] >= inf:
    print(-1)
else:
    print(arr[k])