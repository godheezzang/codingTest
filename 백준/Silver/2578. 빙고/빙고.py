
arr = [list(map(int, input().split())) for _ in range(5)]
bingo = [list(map(int, input().split())) for _ in range(5)]


def check_bingo():
    global cnt
    fake = 0
    # 가로
    for i in range(5):
        if all(arr[i][j] == 'x' for j in range(5)):
            fake += 1
    # 세로
    for i in range(5):
        if all(arr[j][i] == 'x' for j in range(5)):
            fake += 1
    # 대각선
    if all(arr[i][i] == 'x' for i in range(5)):
        fake += 1
    if all(arr[i][4 - i] == 'x' for i in range(5)):
        fake += 1

    if fake != cnt:
        cnt = fake
        return cnt
    return 0


row = 0
col = 0
ret = 0
cnt = 0
for n in range(5):
    for m in range(5):
        for i in range(5):
            for j in range(5):
                if arr[i][j] == bingo[n][m]:
                    arr[i][j] = 'x'
                    if cnt < 3:
                        ret = check_bingo()
                        if ret >= 3:
                            row = n
                            col = m
                            break
            if ret >= 3:
                break
        if ret >= 3:
            break
    if ret >= 3:
        break

# print(row)
# print(col)
print(row * 5 + col + 1)