def solve():
    base = [[0] * 100 for _ in range(100)] # 도화지 =  100 * 100 크기 리스트 생성
    n = int(input())
    # print('n:', n)
    for i in range(n):
        x, y = map(int, input().split())
        # print(x, y)
        for dx in range(10):
            # print('dx:', dx)
            for dy in range(10):
                base[x + dx][y+ dy] = 1 # 10 * 10 크기의 사각형을 1로 채움
    # base에 남아있는 1의 개수 채우기
    # 2차원 리스트에서 전체 합을 구할 때 쓰는 문법
              # 다 더한 값을 한 줄씩 채워 넣기
         # 한줄씩 더해진 값을 다 더하기
    print(sum(sum(line) for line in base))

solve()