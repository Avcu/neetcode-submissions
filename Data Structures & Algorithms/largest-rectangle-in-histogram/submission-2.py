class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lArr = [-1] * len(heights)
        stack = []
        for idx in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[idx]:
                stack.pop()
            if stack:
                lArr[idx] = stack[-1]
            stack.append(idx)

        stack = []
        rArr = [len(heights)] * len(heights)
        for idx in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[idx]:
                stack.pop()
            if stack:
                rArr[idx] = stack[-1]
            stack.append(idx)

        maxArea = 0
        for idx in range(len(heights)):
            currArea = heights[idx]*(rArr[idx]-lArr[idx]-1)
            maxArea = max(maxArea, currArea)

        return maxArea