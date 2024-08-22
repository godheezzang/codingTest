
switch = [None] + list(input())
result = 0

for i in range(1, len(switch)):
    if switch[i] == 'Y':
        for j in range(i, len(switch), i):
            if switch[j] == 'Y':
                switch[j] = 'N'
            else: switch[j] = 'Y'

        result += 1

print(result)