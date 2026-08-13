class Solution:
    def trap(self, height: List[int]) -> int:
        leftToRight = []
        for idx in range(len(height)):
            if idx == 0:
                leftToRight.append(0)
            else:
                if leftToRight[-1] > height[idx-1]:
                    leftToRight.append(leftToRight[-1])
                else:
                    leftToRight.append(height[idx-1])
        
        rightToLeft = []
        for idx in range(1,len(height)+1):
            if idx == 1:
                rightToLeft.append(0)
            else:
                if rightToLeft[-1] > height[-idx+1]:
                    rightToLeft.append(rightToLeft[-1])
                else:
                    rightToLeft.append(height[-idx+1])

        rightToLeft.reverse()
        res = 0
        for idx in range(len(height)):
            if min(leftToRight[idx], rightToLeft[idx]) > height[idx]:
                res += min(leftToRight[idx], rightToLeft[idx]) - height[idx]
        return res

                