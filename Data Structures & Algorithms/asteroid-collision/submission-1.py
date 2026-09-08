class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for idx in range(len(asteroids)):
            curVal = asteroids[idx]
            curPos = curVal > 0
            isExploded = False

            while stack and stack[-1] > 0 and not curPos:
                lastVal = stack[-1]
                if lastVal < -curVal:
                    stack.pop()
                elif lastVal == -curVal:
                    stack.pop()
                    isExploded = True
                    break
                else:
                    isExploded = True
                    break

            if not isExploded:
                stack.append(curVal)
            
        return stack