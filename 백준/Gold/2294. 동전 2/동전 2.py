n, k = map(int, input().split())
coins = [0]
inf = int(21e8)
arr = [[inf] * (k+1) for _ in range(n+1)]
for i in range(n):
    value = int(input())
    coins.append(value)

coins.sort()

# 나누어서 딱 떨어진다 -> 몫을 배열에 넣어준다
# 딱 떨어지지 않는다 -> 몫과 이전에 나눠줬던걸 더해서 더 작은걸 값에 넣는다.
for i in range(1, n+1):
    for j in range(1, k+1):
        if j % coins[i] == 0:
            arr[i][j] = j // coins[i]
        else:
            if j//coins[i] == 0:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = min(arr[i-1][j], arr[i][j-coins[i]]+1)

if arr[n][k] == inf:
    print(-1)
else:
    print(arr[n][k])