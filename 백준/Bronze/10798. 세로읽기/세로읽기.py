def solve():
    arr = []
    for _ in range(5):
        line = input().strip()
        arr.append(list(line))
    # print(arr)

    # 대각선으로 대칭이동한 새로운 배열 만들기
    for i in range(15):
        for j in range(5):
            # 만약 문자열 길이보다 열 index가 작다면
            if i < len(arr[j]):
                print(arr[j][i], end = "") # 공백없이 출력

solve()