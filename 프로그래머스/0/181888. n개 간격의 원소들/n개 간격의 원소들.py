def solution(num_list, n):
    # num_list[시작 인덱스(안쓰면 0):끝 인덱스(안쓰면 리스트 끝까지):건너뛰는 간격]
    return num_list[::n]
