# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.maxAmount = 0

        def dfs(root):
            if root is None:
                return [0, 0]
            
            left1, left2 = dfs(root.left)
            right1, right2 = dfs(root.right)

            curr1 = left2 + right2 + root.val
            curr2 = max(left1, left2) + max(right1, right2)
            return [curr1, curr2]

        resValues = dfs(root)
        return max(resValues[0], resValues[1])
