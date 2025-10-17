

def solution(num_list):
    for n in range(len(num_list)):
        if num_list[n] < 0:
            return n
    return -1