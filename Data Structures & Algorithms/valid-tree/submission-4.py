from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        seen = set()
        q = deque()
        q.append([0, -1])
        seen.add(0)

        while q:
            child, parent = q.popleft()

            for nei in adj[child]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                q.append([nei, child])
                seen.add(nei)
        return len(seen) == n