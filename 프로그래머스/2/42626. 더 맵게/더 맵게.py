
def solution(scoville, K):
    import heapq
    ans = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        Mix = (heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, Mix)
        ans += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return ans