def solve():
    n = int(input())
    # 점수를 받아 리스트에 담음
    scores = list(map(int, input().split()))
    # 그 중 최대 점수
    best_score = max(scores)
    # 조작 점수 계산하기 -> 반복문 돌려서 각 점수 조작
    fake_scores = [i / best_score*100 for i in scores]
    # 새로운 평균 구하기
    avg = sum(fake_scores) / n
    print(avg)
solve()