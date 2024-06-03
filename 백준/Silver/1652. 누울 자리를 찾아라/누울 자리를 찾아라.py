

def solve():
    n = int(input()) # 방의 크기 입력받기
    room = []
    for _ in range(n):
        luggage = input().strip()
        room.append(list(luggage)) # 방의 구조 구하기

    # 가로로 누울 수 있는 자리
    # ".""."이 연속해서 2개 이상 -> ".", ".", "X" 부터 누울 수 있음
    width = 0
    for i in range(n):
        space = 0 # 누울 공간
        for j in range(n):
            if room[i][j] == ".":
                space += 1
                # 2개가 될 경우
                if space == 2:
                    width += 1 # 가로로 누울 공간 추가
            else:
                space = 0
                continue
    # 세로로 누울 수 있는 자리
    height = 0
    for i in range(n):
        space = 0
        for j in range(n):
            if room[j][i] == ".": # 세로니까
                space += 1
                if space == 2:
                    height += 1
            else:
                space = 0
                continue
    print(width, height)

solve()