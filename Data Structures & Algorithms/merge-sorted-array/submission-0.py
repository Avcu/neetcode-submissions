class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        numsA = nums1[:m]   # len: m
        numsB = nums2       # len: n
        idxA, idxB = 0, 0
        currIdx = 0

        while idxA < m and idxB < n:
            nextA = numsA[idxA]
            nextB = numsB[idxB]

            if nextA < nextB:
                nums1[currIdx] = nextA
                currIdx += 1
                idxA += 1
            else:
                nums1[currIdx] = nextB
                currIdx += 1
                idxB += 1
        if idxB == n:
            nums1[currIdx:] = numsA[idxA:]
        if idxA == m:
            nums1[currIdx:] = numsB[idxB:]
