t = int(input())
for case in range(1, t+1):
    student = list(map(int, input().split()))
    cnt = 0
    for i in range(1, len(student)-1):
        for j in range(i+1, len(student)):
            if student[i] > student[j]:
                student[i], student[j] = student[j], student[i]
                cnt += 1
    print(case, cnt)