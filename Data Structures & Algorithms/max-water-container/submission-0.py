class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxWater = min(heights)
        while l < r:
            if heights[l] < heights[r]:
                maxWater = max(maxWater, (r-l)*heights[l])
                l += 1
            else:
                maxWater = max(maxWater, (r-l)*heights[r])
                r -= 1
        return maxWater