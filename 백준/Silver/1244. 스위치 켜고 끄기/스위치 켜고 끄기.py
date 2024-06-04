
def switch_onoff(index):
    if switch[index] == 0:
        switch[index] = 1
    else:
        switch[index] = 0


n = int(input())
switch = [None] + list(map(int, input().split()))
students = int(input())

for i in range(students):
    gender, num = map(int, input().split())
    # 남자
    if gender == 1:
        for j in range(num, n+1, num):
            switch_onoff(j)
    # 여자
    elif gender == 2:
        switch_onoff(num)
        for k in range(n // 2):
            if (num + k > n) or (num - k < 1):
                break
            if switch[num + k] == switch[num - k]:
                switch_onoff(num + k)
                switch_onoff(num - k)
            else:
                break

for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()

