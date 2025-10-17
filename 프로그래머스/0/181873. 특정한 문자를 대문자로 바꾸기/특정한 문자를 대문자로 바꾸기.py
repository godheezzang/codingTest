def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i.lower() == alp:
            answer += alp.upper()
        else:
            answer += i

    return answer