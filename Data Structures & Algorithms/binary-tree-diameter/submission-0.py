# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(root):
            if root is None:
                return 0
            else:
                leftHeight = dfs(root.left)
                rightHeight = dfs(root.right)
                if leftHeight + rightHeight > self.diameter:
                    self.diameter = leftHeight + rightHeight
                return max(leftHeight, rightHeight) + 1
        
        dfs(root)
        return self.diameter

