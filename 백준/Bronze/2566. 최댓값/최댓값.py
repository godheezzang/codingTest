

def solve():
    arr = [list(map(int, input().split())) for _ in range(9)] # 입력 받은 수로 9 * 9 배열 만들기
    # print(arr)

    max_num = max(map(max, arr)) # 최댓값 찾기
    print(max_num)

    for i, row in enumerate(arr):
        # print('row:', row)
        for j, col in enumerate(row):
            # print('col:', col)
            if col == max_num:
                print(i+1, j+1) # i, j번째에서 +1한 값이 답으로 나오길래...더함,,,, 왜일까.....

solve()