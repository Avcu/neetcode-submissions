from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minDict = defaultdict(int)
        adj = [[] for _ in range(n+1)]

        for t in times:
            adj[t[0]].append([t[1], t[2]])

        q = deque()
        q.append(k)
        minDict[k] = 0

        while q:
            cur = q.popleft()
            curDist = minDict[cur]

            for nei, neiDist in adj[cur]:
                if nei not in minDict or curDist + neiDist < minDict[nei]:
                    minDict[nei] = curDist + neiDist
                    q.append(nei)
        
        return -1 if len(minDict) != n else max(minDict.values())

                