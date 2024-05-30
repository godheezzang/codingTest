from collections import Counter
def solve():
    n = int(input())
        # 확장자 구분해서 변수에 담기
    extensions = [input().split(".")[1] for i in range(n)]
        # 확장자가 몇 개인지 파악 위해 Counter 사용
    extensions_count = Counter(extensions)
        # items() -> 딕셔너리 key-value 쌍 반환
        # sorted() -> 사전 순으로 정렬
    for name, count in sorted(extensions_count.items()):
        print(name, count)
solve()