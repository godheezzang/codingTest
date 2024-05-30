def solve():
    # n만큼 이름과 상태 입력 받기
    n = int(input())
    # 이름=상태 형식의 딕셔너리 생성
    log = {}

    # 상태가 "leave"라면 value = 0, "enter"면 value=1
    for i in range(n):
        name, state = input().split()
        if state == "leave":
            log[name] = 0
        else:
            log[name] = 1
    # value가 1인 name을 찾아 active_members에 담기
    active_members = [ name for name in log if log[name] == 1]
    
    # 역순 출력
    for name in sorted(active_members, reverse=True):
        print(name)
solve()