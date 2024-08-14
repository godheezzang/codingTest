
arr = [[0] * 101 for _ in range(101)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for dy in range(y, y+10):
        for dx in range(x, x+10):
            arr[dy][dx] = 1

# for _ in arr:
#     print(*_, end='\n', sep=' ')

total = 0
direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            temp = 0
            for k in range(4):
                if arr[i+direct_y[k]][j+direct_x[k]] == 1:
                    temp += 1

            # 둘레/모서리 겹치는 부분 생각?????????????
            if temp == 3: total += 1
            elif temp == 2: total += 2

print(total)