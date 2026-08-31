class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s: str):
            return s == s[::-1]

        resList = []

        def dfs(strIte, curr, cnt):
            if cnt == len(s):
                resList.append(curr.copy())
                return

            n = len(strIte)
            for idx in range(1, n+1):
                if isPal(strIte[:idx]):
                    curr.append(strIte[:idx])
                    dfs(strIte[idx:], curr, cnt+len(strIte[:idx]))
                    curr.pop()

        dfs(s, [], 0)
        return resList