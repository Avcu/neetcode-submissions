from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapify(heap)

        while len(heap) > 1:
            stone1 = -heappop(heap)
            stone2 = -heappop(heap)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heappush(heap, stone2-stone1)
            else:
                heappush(heap, stone1-stone2)
        
        return -heap[0] if len(heap) == 1 else 0
