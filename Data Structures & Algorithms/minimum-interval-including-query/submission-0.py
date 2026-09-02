from heapq import heappop, heappush

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        qSorted = sorted(queries)
        resDict = {}
        minHeap = []

        idx = 0
        for q in qSorted:
            while idx < len(intervals) and intervals[idx][0] <= q:
                lenInterval = intervals[idx][1] - intervals[idx][0] + 1
                heappush(minHeap, [lenInterval, intervals[idx][1]])
                idx += 1
            
            while minHeap and minHeap[0][1] < q:
                heappop(minHeap)

            if minHeap:
                resDict[q] = minHeap[0][0]
            else:
                resDict[q] = -1
        
        return [resDict[q] for q in queries]
        
