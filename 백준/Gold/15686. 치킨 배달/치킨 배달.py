
from itertools import combinations

# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# (r1, c1), (r2, c2)가 있을 때 치킨 거리 = |r1 - r2| + |c1 - c2|

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

def distance(h, c):
    return abs(h[0] - c[0]) + abs(h[1] - c[1])

# 그럼 이제 치킨집을 고르고.. 가장 작은 치킨거리를 구해야 한다
min_chicken_distance = float('inf')

for s_c in combinations(chicken, m):
    chicken_distance = 0
    for h in house:
        min_distance = float('inf')
        for c in s_c:
            min_distance = min(min_distance, distance(h, c))
        chicken_distance += min_distance
    min_chicken_distance = min(min_chicken_distance, chicken_distance)

print(min_chicken_distance)