class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpList = [False] * len(nums)

        for idx in range(len(nums)):
            if idx == 0:
                jump = nums[idx]
                jumpList[idx:idx+jump+1] = [True] * (jump+1)
            else:
                if jumpList[idx]:
                    jump = nums[idx]
                    jumpList[idx:idx+jump+1] = [True] * (jump+1)
                else:
                    return False
        return jumpList[-1]
        