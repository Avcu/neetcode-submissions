from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minDict = defaultdict(int)
        adj = [[] for _ in range(n+1)]

        for t in times:
            adj[t[0]].append([t[1], t[2]])

        # (weight, node)
        minHeap = [(0, k)]

        while minHeap:
            curW, curNode = heappop(minHeap)

            if curNode in minDict:
                continue
            minDict[curNode] = curW

            for nei, neiW in adj[curNode]:
                if nei not in minDict:
                    heappush(minHeap, (curW+neiW, nei))

        
        return -1 if len(minDict) != n else max(minDict.values())

                