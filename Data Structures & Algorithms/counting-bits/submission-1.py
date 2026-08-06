class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBitsGivenInt(intInput: int):
            binN = bin(intInput)
            counter = 0
            for ch in binN:
                if ch == '1':
                    counter += 1
            return counter

        bitCountList = []
        for idx in range(n+1):
            bitCountList.append(countBitsGivenInt(idx))
        return bitCountList
