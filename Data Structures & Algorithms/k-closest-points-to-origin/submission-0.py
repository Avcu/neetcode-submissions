from heapq import heapify, heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            currDistance = point[0]**2 + point[1]**2
            heappush(heap, [-currDistance, point])

            if len(heap) > k:
                heappop(heap)
        
        return [x[1] for x in heap]