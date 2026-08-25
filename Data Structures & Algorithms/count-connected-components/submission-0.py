class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [0 for _ in range(n)]
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        
        def dfs(idx):
            if visited[idx] == 1:
                return
            else:
                visited[idx] = 1
                for neighbor in adj[idx]:
                    dfs(neighbor)

        resCount = 0
        for idx in range(n):
            if visited[idx] == 0:
                resCount += 1
                dfs(idx)

        return resCount