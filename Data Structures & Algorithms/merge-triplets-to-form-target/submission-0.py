class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        newTriplets = []

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                newTriplets.append([x, y, z])
        
        xAll, yAll, zAll = 0, 0, 0
        for x, y, z in newTriplets:
            xAll = max(xAll, x)
            yAll = max(yAll, y)
            zAll = max(zAll, z)

        return xAll == target[0] and yAll == target[1] and zAll == target[2]