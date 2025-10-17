str = input()

def solve(str):
    result = ''
    for n in str:
        if ord('a') <= ord(n) <= ord('z'):
            result += n.upper()
        else:
            result += n.lower()
    return result

print(solve(str))