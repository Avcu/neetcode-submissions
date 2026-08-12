from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # lower half
        self.minHeap = [] # upper half

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0:
            heappush(self.minHeap, num)
        else:
            minVal = self.minHeap[0]
            if num < minVal:
                heappush(self.maxHeap, -num)
            else:
                heappush(self.minHeap, num)

        while len(self.maxHeap) < len(self.minHeap) - 1:
            poppedVal = heappop(self.minHeap)
            heappush(self.maxHeap, -poppedVal)

        while len(self.minHeap) < len(self.maxHeap):
            poppedVal = heappop(self.maxHeap)
            heappush(self.minHeap, -poppedVal)
            

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0]+self.minHeap[0])/2
        else:
            return self.minHeap[0]
        