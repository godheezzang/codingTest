def solve():
  num1, num2 = map(int, input().split())
  # 수를 거꾸로 읽게 하기 위해, 문자열로 바꾼 후 슬라이싱 사용, 그리고 다시 정수형 변환
  reserved_num1 = int(str(num1)[::-1])
  reserved_num2 = int(str(num2)[::-1])
  # max()로 큰 수 찾기
  big_num = max(reserved_num1, reserved_num2)
  print(big_num)
solve()