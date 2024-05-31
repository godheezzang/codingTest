
# 알고리즘 파이썬으로 변경

def MenOfPassion(A, n):
    sum = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                sum += A[i] * A[j] * A[k]
    return sum

n = int(input())
# 전체 수행 횟수 = 1부터 n-2까지, 각 1부터 해당 값까지 합의 결과를 모두 더한 값
print((n * (n-1) * (n-2)) // 6)

# 최고차항의 차수
print(3)