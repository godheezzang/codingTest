n = int(input())
a = 1
max_cnt = 0
result = []
while a <= n:
    arr = [n]
    arr.append(a)
    while arr[-2] - arr[-1] >= 0:
        arr.append(arr[-2] - arr[-1])
    if max_cnt < len(arr):
        max_cnt = len(arr)
        result = arr
    a += 1

print(max_cnt)
for i in range(len(result)):
    print(result[i], end=' ')