
n, k = map(int, input().split())
objects = [[0, 0]]
for i in range(n):
    w, v = map(int, input().split())
    objects.append([w, v])

objects.sort(key=lambda x: x[0])
arr = [[0] * (k+1) for _ in range(n+1)]
# arr[i][j] = arr[무게][가치]
# arr[3][가치] = 6
# 만약 넣을 물건의 가치가 arr[무게][가치]보다 작으면 이전 무게의 값으로 넣고
# 크다면 대체
# 만약 무게가 이전 무게+현재 넣을 물건의 무게와 같다면, 가치는 더한다

for i in range(1, n+1): # 아이템 개수
    for j in range(1, k+1): # 가방에 담을 수 있는 무게
        weight = objects[i][0] # 아이템의 무게
        value = objects[i][1] # 아이템 가치
        if j < weight: # 가방에 해당 아이템을 담을 수 없다면
            arr[i][j] = arr[i-1][j] # 사전 단계에서 얻었던 값을 넣기
        else: # j 무게에 해당 물건을 넣을 수 있는 경우
            # 사전 단계에서 얻은 최대치 vs 물건 하나 담았을 때 만족도+남은 무게에 대한 만족도의 최대값
            arr[i][j] = max(arr[i-1][j], value + arr[i-1][j-weight])


print(arr[n][k])