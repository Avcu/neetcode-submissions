class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        myStack = []
        for idx in range(len(temperatures)):
            currVal = temperatures[idx]
            while myStack:
                lastIdx = myStack[-1][0]
                lastVal = myStack[-1][1]
                if lastVal < currVal:
                    res[lastIdx] = idx - lastIdx
                    myStack.pop()
                else:
                    break
            myStack.append(tuple([idx, currVal]))
        return res
                