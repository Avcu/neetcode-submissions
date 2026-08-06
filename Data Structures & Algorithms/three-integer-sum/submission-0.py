class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resSet = set()

        nums.sort()

        for idx in range(len(nums)):
            num1 = nums[idx]

            if num1 > 0:
                break
            else:
                l, r = idx+1, len(nums)-1
                while l < r:
                    num2 = nums[l]
                    num3 = nums[r]
                    if num2+num3 == -num1:
                        resSet.add(tuple([num1, num2, num3]))
                        l += 1
                    elif num2+num3 < -num1:
                        l += 1
                    else:
                        r -= 1
        return list(resSet)