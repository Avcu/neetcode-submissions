from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0

        for _ in range(k+1):
            newCost = cost.copy()

            for u, v, price in flights:
                if cost[u] != float('inf'):
                    newCost[v] = min(newCost[v], cost[u] + price)

            cost = newCost

        return -1 if cost[dst] == float('inf') else cost[dst]