class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resList = []

        def dfs(idx, arr, total):
            if total == target:
                resList.append(arr.copy())
                return
            if total > target or idx >= len(nums):
                return

            arr.append(nums[idx])
            dfs(idx, arr, total+nums[idx])
            arr.pop()
            dfs(idx+1, arr, total)

        dfs(0, [], 0)
        return resList
            
