class Solution:
    def hammingWeight(self, n: int) -> int:
        binN = bin(n)
        counter = 0
        for ch in binN:
            if ch == '1':
                counter += 1
        return counter