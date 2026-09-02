class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}

        tickets.sort()
        tickets = tickets[::-1]
        for u, v in tickets:
            adj[u].append(v)

        res = []
        def dfs(u):
            while u in adj and adj[u]:
                nei = adj[u].pop()
                dfs(nei)
            res.append(u)
        
        dfs("JFK")
        res.reverse()
        return res
                