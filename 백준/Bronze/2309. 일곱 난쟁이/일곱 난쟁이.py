arr = [int(input()) for _ in range(9)]
lie_dwarf = []

for i in range(9):
    for j in range(9):
        if i == j: continue
        if sum(arr) - (arr[i]+arr[j]) == 100:
            lie_dwarf.append(arr[i])
            lie_dwarf.append(arr[j])
        if len(lie_dwarf) == 2:
            break

arr.remove(lie_dwarf[0])
arr.remove(lie_dwarf[1])
arr.sort()

for i in range(len(arr)):
    print(arr[i])