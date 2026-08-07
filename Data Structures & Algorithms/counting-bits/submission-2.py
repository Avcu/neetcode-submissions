class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(n):
            cnt = 0
            for i in range(32):
                cnt += 1 if (1 << i) & n else 0
            return cnt
        
        return [countOnes(i) for i in range(n+1)]