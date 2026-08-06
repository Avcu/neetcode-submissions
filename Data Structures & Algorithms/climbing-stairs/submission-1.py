class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n+1)
        for idx in range(n+1):
            if idx == 1 or idx == 2:
                arr[idx] = idx
            else:
                arr[idx] = arr[idx-1] + arr[idx-2]
        return arr[idx]        