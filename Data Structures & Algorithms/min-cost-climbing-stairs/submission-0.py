class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0] * len(cost)
        for idx in range(len(cost)):
            if idx == 0 or idx == 1:
                arr[idx] = cost[idx]
            else:
                arr[idx] = min(arr[idx-1], arr[idx-2]) + cost[idx]
        return min(arr[-1], arr[-2])