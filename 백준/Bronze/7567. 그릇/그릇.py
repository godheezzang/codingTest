dishes = input().strip()

dishes_height = 10
for i in range(1, len(dishes)):
    if dishes[i] == dishes[i - 1]:
        dishes_height += 5
    else:
        dishes_height += 10

print(dishes_height)