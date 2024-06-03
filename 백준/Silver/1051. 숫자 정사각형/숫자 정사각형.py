def solve():
    # 2차원 배열 생성
    arr = []
    row, col = map(int, input().split())
    for _ in range(row):
        line = input().strip()
        arr.append(list(line))

    # row * col 사이즈의 직사각형 내에서 생기는 정사각형은 row, col보다 클 수 없음
    # 정사각형의 최대 길이 = row, col 중 작은 수의 길이
    len = min(row, col)
    ans = 1 # 최소 정사각형의 크기

    # 가로 길이 = row - len
    # 세로 길이 = col - len
    # 넓이 = len ** 2
    for i in range(row):
        # print('i:', i)
        for j in range(col):
            for k in range(len):
                # print('k:', k)
                if ((i+k) < row) and ((j+k) < col) and arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]:
                    ans = max(ans, (k+1) ** 2)
    print(ans)

solve()