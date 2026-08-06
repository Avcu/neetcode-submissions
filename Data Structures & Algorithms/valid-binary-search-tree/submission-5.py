# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.validBST = True

        # traverse the tree while checking if all the values are less then maxValue and greater than minValue
        def dfs(root, minValue, maxValue):
            if not root:
                return True
            if root.val <= minValue or root.val >= maxValue:
                self.validBST = False
            dfs(root.left, minValue=minValue, maxValue=root.val)
            dfs(root.right, minValue=root.val, maxValue=maxValue)

        dfs(root, minValue=-float('inf'), maxValue=float('inf'))
        return self.validBST