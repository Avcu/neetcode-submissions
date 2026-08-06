class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumDict = {}
        for idx in range(len(nums)):
            num = nums[idx]
            diff = target - num

            # look for exit condition
            if diff in twoSumDict:
                return [twoSumDict[diff], idx]
            else:
                if num in twoSumDict:
                    continue
                else:
                    twoSumDict[num] = idx
                