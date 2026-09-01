class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            if par[n] == n:
                return n
            par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
            return True

        edges = []
        for i in range(n):
            for j in range(i+1, n):
                currDist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append([currDist, i, j])
        edges.sort()


        res = 0
        for dist, u, v in edges:
            if union(u, v):
                res += dist
        return res