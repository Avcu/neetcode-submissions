class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodeDict = {}
        idx = 0

        for u, v in equations:
            if u not in nodeDict:
                nodeDict[u] = idx
                idx += 1
            if v not in nodeDict:
                nodeDict[v] = idx
                idx += 1

        n = idx
        adj = [[] for _ in range(n)]


        for i in range(len(equations)):
            val = values[i]
            u, v = equations[i]
            u, v = nodeDict[u], nodeDict[v]

            adj[u].append([v, val])
            adj[v].append([u, 1.0/val])

        resList = []
        for u, v in queries:
            if u not in nodeDict or v not in nodeDict:
                resList.append(-1)
                continue
            u, v = nodeDict[u], nodeDict[v]
            stack = [[u, 1]]
            seen = set()
            isFound = False

            while stack and not isFound:
                cur, curVal = stack.pop()
                if cur == v:
                    res = curVal
                    isFound = True
                seen.add(cur)

                for nei, neiVal in adj[cur]:
                    if nei not in seen:
                        stack.append([nei, curVal*neiVal])

            if not isFound:
                res = -1
            resList.append(res)
        return resList
