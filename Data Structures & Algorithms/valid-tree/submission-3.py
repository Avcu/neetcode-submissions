class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        seen = set()
        q = []
        q.append([-1, 0]) # parent and then child

        while q:
            parent, child = q.pop()

            for e in adj[child]:
                if e == parent:
                    continue
                if e in seen:
                    return False
                q.append([child, e])
            seen.add(child)
        return len(seen) == n