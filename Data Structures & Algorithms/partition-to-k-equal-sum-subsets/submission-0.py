class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        usedList = [False] * len(nums)

        totSum = sum(nums)
        if totSum % k != 0:
            return False
        target = totSum // k

        nums.sort(reverse=True)
        def dfs(i, k, curSum):
            if k == 0:
                return True
            if curSum == target:
                # start a new search
                return dfs(0, k-1, 0)

            for j in range(i, len(nums)):
                if not usedList[j] and curSum + nums[j] <= target:
                    usedList[j] = True
                    if dfs(j+1, k, curSum+nums[j]):
                        return True
                    usedList[j] = False
            return False

        return dfs(0, k, 0)
