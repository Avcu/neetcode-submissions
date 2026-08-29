class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1 or sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        memo = [[-1]*(target+1) for _ in range(len(nums)+1)]

        def dfs(i, total):
            if total == target:
                return True
            if i >= len(nums) or total > target:
                return False
            if memo[i][total] != -1:
                return memo[i][total]

            takeI = dfs(i+1, total+nums[i])
            skipI = dfs(i+1, total)
            memo[i][total] = takeI or skipI
            return memo[i][total]
        
        return dfs(0, 0)