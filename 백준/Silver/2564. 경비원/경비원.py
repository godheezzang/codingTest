
w, h = map(int, input().split())
n = int(input())
s_location = []
for i in range(n):
    direction, distance = map(int, input().split())
    s_location.append([direction, distance])

d_location = list(map(int, input().split()))

total = 0

for i in range(n):
    # 북쪽일 때
    if s_location[i][0] == 1: continue
    # 남쪽일 때
    if s_location[i][0] == 2:
        s_location[i][1] = w+h+(w-s_location[i][1])
    # 서쪽일 때
    if s_location[i][0] == 3:
        s_location[i][1] = (2*w)+h+(h-s_location[i][1])
    # 동쪽일 때
    if s_location[i][0] == 4:
        s_location[i][1] = w+s_location[i][1]

# 동근이의 0, 0 기준 거리 계산
if d_location[0] == 2:
    d_location[1] = w+h+(w-d_location[1])
elif d_location[0] == 3:
    d_location[1] = (2*w)+h+(h-d_location[1])
elif d_location[0] == 4:
    d_location[1] = w+d_location[1]

for i in range(n):
    total += min(abs(s_location[i][1]-d_location[1]), ((2*w)+(2*h))-abs(s_location[i][1]-d_location[1]))

print(total)