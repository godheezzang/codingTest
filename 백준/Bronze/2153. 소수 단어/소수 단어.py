import sys
input = sys.stdin.readline

# 문자 총합 계산
def alphabet_value(word):
    total = 0
    for char in word:
        if 'a' <= char <= 'z':
            total += ord(char) - ord('a') + 1
        elif 'A' <= char <= 'Z':
            total += ord(char) - ord('A') + 27
    return total

word = input().strip()
value = alphabet_value(word)

# 소수 판별 함수
def is_prime(value):
    if value == 1:
        return True
    elif value < 2:
        return False
    elif value == 2:
        return True
    elif value % 2 == 0:
        return False
    for i in range(3, int(value ** 0.5) + 1, 2): # 홀수 소수 구분
        if value % i == 0:
            return False
    return True

if is_prime(value):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
