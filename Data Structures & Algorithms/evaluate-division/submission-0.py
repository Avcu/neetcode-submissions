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
            if u == v:
                resList.append(1)
                continue

            stack = [[u, -1, 1]]
            seen = set()
            isFound = False

            while stack and not isFound:
                cur, p, curVal = stack.pop()
                seen.add(cur)

                for nei, neiVal in adj[cur]:
                    if nei == p:
                        continue
                    if nei == v:
                        res = curVal * neiVal
                        isFound = True
                        break
                    else:
                        stack.append([nei, cur, curVal*neiVal])
            if not isFound:
                res = -1
            resList.append(res)
        return resList
