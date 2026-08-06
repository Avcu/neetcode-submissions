# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodeCount = 0

        def dfs(root, maxValue):
            if root is None:
                return 0
            else:
                if root.val > maxValue:
                    maxValue = root.val
                if root.left is not None and root.left.val >= maxValue:
                    self.goodNodeCount += 1 
                if root.right is not None and root.right.val >= maxValue:
                    self.goodNodeCount += 1
                dfs(root.left, maxValue)
                dfs(root.right, maxValue)

        dfs(root, -101)
        return self.goodNodeCount + 1
            