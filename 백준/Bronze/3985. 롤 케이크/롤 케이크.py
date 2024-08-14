l = int(input())
n = int(input())
arr = [0] * l
expect_num = ''
max_diff = -21e8
papers = [list(map(int, input().split())) for _ in range(n)]
# 예상 방청객 수
for i in range(n):
    if abs(papers[i][0] - papers[i][1]) > max_diff:
        max_diff = abs(papers[i][0] - papers[i][1])
        expect_num = i+1

# 실제로 많이 받은 방청객 수
for i in range(n):
    a = papers[i][0] - 1
    b = papers[i][1] - 1
    for j in range(a, b+1):
        if arr[j] != 0: continue
        arr[j] = i+1

result = []
# 최다 빈도값 구하기
for i in range(l):
    if arr[i] != 0:
        result.append(arr[i])

real_num = max(set(result), key=result.count)

print(expect_num)
print(real_num)