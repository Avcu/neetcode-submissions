class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateTotalHourUnderH(piles, k, h):
            sumHours = 0
            for pile in piles:
                sumHours += math.ceil(pile/k)
            return sumHours <= h

        l, r = 1, max(piles)
        while l <= r:
            middle = (l+r)//2
            if calculateTotalHourUnderH(piles, middle, h):
                # found the case where k is high enough
                # check if k-1 is also enough
                if middle != 1 and calculateTotalHourUnderH(piles, middle-1, h):
                    r = middle - 1
                else:
                    return middle
            else:
                l = middle + 1
        

