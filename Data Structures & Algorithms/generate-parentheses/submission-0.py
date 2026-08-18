class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            combinations = self.generateParenthesis(n-1)
            newSet = set()

            for combination in combinations:
                for idx in range(len(combination)):
                    newCombination = combination[:idx] + "()" + combination[idx:]
                    newSet.add(newCombination)
            return list(newSet)
        