# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = k
        self.res = -1

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            if self.counter == 0:
                return
            self.counter -= 1
            if self.counter == 0:
                self.res = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.res