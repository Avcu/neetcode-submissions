class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        numsFirstZero = nums.copy()
        arr = [0] * len(nums)
        numsFirstZero[0] = 0
        for idx in range(len(numsFirstZero)):
            if idx == 0:
                arr[idx] = numsFirstZero[idx]
            elif idx == 1:
                arr[idx] = max(numsFirstZero[idx], numsFirstZero[idx-1])
            else:
                arr[idx] = max(arr[idx-1], arr[idx-2]+numsFirstZero[idx])
        resultFirstZero = max(arr[-1], arr[-2])

        numsLastZero = nums.copy()
        arr = [0] * len(nums)
        numsLastZero[-1] = 0
        for idx in range(len(numsLastZero)):
            if idx == 0:
                arr[idx] = numsLastZero[idx]
            elif idx == 1:
                arr[idx] = max(numsLastZero[idx], numsLastZero[idx-1])
            else:
                arr[idx] = max(arr[idx-1], arr[idx-2]+numsLastZero[idx])
        resultLastZero = max(arr[-1], arr[-2])

        return max(resultFirstZero, resultLastZero)