class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        else:
            result = 1
            for idx in range(n):
                result *= x
            return result