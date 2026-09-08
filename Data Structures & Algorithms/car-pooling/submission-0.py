from heapq import heappush, heappop

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))

        minHeap = []
        curCap = capacity

        for i in range(len(trips)):
            # (endTime, capacity)
            heappush(minHeap, (trips[i][2], trips[i][0]))
            curCap -= trips[i][0]

            # remove the trips that ended
            while minHeap and minHeap[0][0] <= trips[i][1]:
                _, poppedCap = heappop(minHeap)
                curCap += poppedCap
            
            if curCap < 0:
                return False
        return True