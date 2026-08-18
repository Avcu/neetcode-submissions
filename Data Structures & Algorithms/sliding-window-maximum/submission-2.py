from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        resList = []

        for i in range(k):
            heappush(window, [-nums[i], i])

        for i in range(k, len(nums)+1):
            val, idx = -window[0][0], window[0][1]
            # ignore the values that are outside of the current window
            while idx < i - k:
                heappop(window)
                val, idx = -window[0][0], window[0][1]
            
            resList.append(val)

            if i < len(nums):
                heappush(window, [-nums[i], i])
        return resList