x, y = map(int, input().split())

def solve(x, y):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    # 1/31 수, 32 목, 33 금, 34 토, 35 일, 36 월, ...
    # 32 목 구하기 위해선? 31(2월의 전 달인 1월 일 수)+1(2월 1일의 일자 1이 필요)
    # 1월 1일과 얼마나 차이나는지 나머지를 구해 비교한 후 무슨 요일인지 구함
    # 7로 나눈 나머지가 1 -> 월, 2 -> 화, 3 -> 수, 4 -> 목, 5 -> 금, 6 -> 토, 0 -> 일
    total = 0

    for i in range(x - 1):
        total += months[i]

    total = (total + y) % 7
    print(days[total - 1])
solve(x, y)