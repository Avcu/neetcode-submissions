class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        charDict = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "r", "q", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"] 
        }
        resList = []
        curr = []
        n = len(digits)

        def dfs(i):
            if len(curr) == n:
                resStr = "".join(curr)
                resList.append(resStr)
                return
                
            curDigit = digits[i]
            for ch in charDict[int(curDigit)]:
                curr.append(ch)
                dfs(i+1)
                curr.pop()

        dfs(0)
        return resList