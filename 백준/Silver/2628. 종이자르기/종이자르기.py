
row_lst = [0]
col_lst = [0]

width, height = map(int, input().split())
row_lst.append(width)
col_lst.append(height)
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 0: col_lst.append(b)
    elif a == 1: row_lst.append(b)

row_lst.sort()
col_lst.sort()

max_row = 0
max_col = 0

for i in range(1, len(row_lst)):
    row = row_lst[i] - row_lst[i-1]
    if row > max_row: max_row = row

for j in range(1, len(col_lst)):
    col = col_lst[j] - col_lst[j-1]
    if col > max_col: max_col = col

print(max_row * max_col)