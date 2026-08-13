class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) < len(B):
            A, B = B, A

        half = (len(A)+len(B)) // 2

        # chose i element from B and half-i from A, binary search on B
        l, r = 0, len(B) - 1
        while True:
            i = (l+r) // 2
            j = half - i - 2

            leftPartition2 = B[i] if i >= 0 else float("-inf")
            rightPartition2 = B[i+1] if i+1 < len(B) else float("inf")
            leftPartition1 = A[j] if j >= 0 else float("-inf")
            rightPartition1 = A[j+1] if j+1 < len(A) else float("inf")

            if leftPartition2 <= rightPartition1 and leftPartition1 <= rightPartition2:
                if (len(A)+len(B)) % 2 == 1:
                    return min(rightPartition1, rightPartition2)
                else:
                    return (max(leftPartition1, leftPartition2)+min(rightPartition1, rightPartition2)) / 2
            elif leftPartition2 > rightPartition1:
                r = i - 1
            else:
                l = i + 1