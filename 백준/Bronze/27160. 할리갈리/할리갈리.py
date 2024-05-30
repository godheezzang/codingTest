def solve():
  n = int(input())
  # 같은 과일의 합계 5가 되면 종을 쳐야 한다.
  # 따라서, 과일의 합을 담아둘 딕셔너리를 만든다.
  cards = {
        'STRAWBERRY': 0,
        'BANANA': 0,
        'LIME': 0,
        'PLUM': 0
  }

  # 입력값으로 받은 문자열과 과일 갯수를 split()을 이용해 쪼갠다.
  # for 문 사용 이유: n번 반복해야 하므로
  # 과일 갯수는 cards[s(=과일 종류)]에 + 해줘야 하므로 += 연산자 사용
  for i in range(n):
      s, x = input().split()
      cards[s] += int(x)
  # 종은 과일 합계가 5개 되어야 칠 수 있음
  # 따라서, cards 딕셔너리 속 값이 5일 때를 bell 변수에 담아둔다.
  bell = 5 in cards.values()
  if bell: print('YES')
  else: print('NO')

solve()
