from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        seen = set()

        def dfs(child, parent):
            seen.add(child)

            res = True
            for nei in adj[child]:
                if nei == parent:
                    continue
                if nei in seen:
                    res = False
                res = res and dfs(nei, child)
            return res

        return dfs(0, -1) and len(seen) == n