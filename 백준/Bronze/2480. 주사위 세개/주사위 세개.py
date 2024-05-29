a, b, c = map(int,input().split())

def price(a, b, c):
    if a == b == c:
        money = 10000 + a * 1000
        print(money)
    elif a == b or a == c:
        money = 1000 + a * 100
        print(money)
    elif b == c:
        money = 1000 + b * 100
        print(money)
    else:
        dice_list = [a, b, c]
        max = 0
        for num in dice_list:
            if max < num:
                max = num
        money = max * 100
        print(money)
        
price(a, b, c)