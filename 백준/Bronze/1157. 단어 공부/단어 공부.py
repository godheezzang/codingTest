
def solve():
    # 대문자로 출력 -> 입력값을 대문자로 받아옴
    word = input().upper()
    # 중복값 제거 후 리스트
    word_list = list(set(word))
    # 많이 나온 빈도수를 담는 빈 리스트
    alphabet = []

    for i in word_list:
        # 입력값에서 알파벳의 빈도수를 셈
        count = word.count(i)
        # 그 값을 빈 리스트에 추가
        alphabet.append(count)

    if alphabet.count(max(alphabet)) >= 2 :
        print("?")
    else:
        print(word_list[alphabet.index(max(alphabet))])
solve()