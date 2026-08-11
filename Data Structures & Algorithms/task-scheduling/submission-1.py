from heapq import heappush, heappop
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [] # (number of tasks, last idx for this task run, task char)
        q = deque()
        dictTaskCount = {}

        for task in tasks:
            if task in dictTaskCount:
                dictTaskCount[task] += 1
            else:
                dictTaskCount[task] = 1
        
        for task, taskCount in dictTaskCount.items():
            heappush(heap, -taskCount)

        currTime = 0
        while heap or q:
            # if there are new available tasks in the queue add them back to heap
            while q and q[0][1] <= currTime:
                poppedQ = q.popleft()
                heappush(heap, poppedQ[0])

            # run the next task in the heap
            if heap:
                poppedVal = heappop(heap)
                if poppedVal != -1:
                    q.append([poppedVal+1, currTime+n+1])
                currTime += 1
            else:
                # if there is no task available wait for the next one in the queue
                poppedQ = q.popleft()
                currTime = poppedQ[1]
                heappush(heap, poppedQ[0])


        return currTime



