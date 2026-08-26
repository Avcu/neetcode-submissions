class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0] * (n+1)
        outDegree = [0] * (n+1)

        for t1, t2 in trust:
            inDegree[t2] += 1
            outDegree[t1] += 1

        for idx in range(1, n+1):
            if inDegree[idx] == n-1 and outDegree[idx] == 0:
                return idx
        return -1