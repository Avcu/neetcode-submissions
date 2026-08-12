# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = root.val

        def dfs(node):
            if not node:
                return [0, 0]
            else:
                [left1, left2] = dfs(node.left)
                [right1, right2] = dfs(node.right)

                curr2 = node.val + left1 + right1
                curr1 = node.val + max(left1, right1, 0)

                if curr2 > self.maxPath:
                    self.maxPath = curr2
                if curr1 > self.maxPath:
                    self.maxPath = curr1

                return [curr1, curr2]
        
        dfs(root)
        return self.maxPath