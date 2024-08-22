
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
cx1, cy1, cx2, cy2 = map(int, input().split())
dx1, dy1, dx2, dy2 = map(int, input().split())

board = [[0] * 101 for _ in range(101)]

for i in range(ay1, ay2):
    for j in range(ax1, ax2):
        board[i][j] = 1

for i in range(by1, by2):
    for j in range(bx1, bx2):
        board[i][j] = 1

for i in range(dy1, dy2):
    for j in range(dx1, dx2):
        board[i][j] = 1

for i in range(cy1, cy2):
    for j in range(cx1, cx2):
        board[i][j] = 1

result = 0
for k in range(101):
    for m in range(101):
        if board[k][m] == 1:
            result += 1

print(result)