# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val=val)

        def dfs(root, val):
            if val >= root.val:
                if root.right is None:
                    newRight = TreeNode(val=val)
                    root.right = newRight
                else:
                    dfs(root.right, val)
            else:
                if root.left is None:
                    newLeft = TreeNode(val=val)
                    root.left = newLeft
                else:
                    dfs(root.left, val)

        dfs(root, val)
        return root