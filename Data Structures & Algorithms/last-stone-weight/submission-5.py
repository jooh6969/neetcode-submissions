import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            diff = first - second
            if diff:
                heapq.heappush(heap, -diff)
        if not heap:
            return 0
        else:
            return -heap[0]
        