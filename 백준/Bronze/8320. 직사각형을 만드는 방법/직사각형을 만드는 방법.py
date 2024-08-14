n = int(input())

k = 1
cnt = 0
while k ** 2 <= n:
    for i in range(k, (n//k)+1):
        # print('i:', i)
        cnt += 1
    k += 1

print(cnt)