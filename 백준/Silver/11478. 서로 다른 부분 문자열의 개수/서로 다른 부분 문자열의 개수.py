
def solve():
    string = input()
    total = set()
        # 부분 문자열 구하기
    for i in range(len(string)):
            # i번째부터 부분 문자열 구한 후 total에 추가
        for j in range(i, len(string)):
            total.add(string[i:j+1])

    print(len(total))
solve()