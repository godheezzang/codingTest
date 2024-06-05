

import sys
input = sys.stdin.readline

n = int(input())
sticks = [] # 막대기 높이 저장

for _ in range(n):
    sticks.append(int(input()))

visible_sticks = 0
stack = []


for height in sticks[::-1]:
    # stack이 없거나 높이가 맨 끝 스틱의 높이보다 클 때 stack에 추가, 보이는 막대기 개수 증가
    if not stack or height > stack[-1]:
        stack.append(height)
        visible_sticks += 1

print(visible_sticks)