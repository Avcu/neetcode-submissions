class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        numsA = nums1[:m]   # len: m
        numsB = nums2       # len: n
        idxA, idxB = 0, 0
        currIdx = 0

        while currIdx < m + n:
            if idxB >= n or (idxA < m and numsA[idxA] <= numsB[idxB]):
                nums1[currIdx] = numsA[idxA]
                idxA += 1
            else:
                nums1[currIdx] = numsB[idxB]
                idxB += 1
            currIdx += 1