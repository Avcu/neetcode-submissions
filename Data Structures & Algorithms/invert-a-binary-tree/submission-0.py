# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            invertedTree = TreeNode(val=root.val)
            if root.right is not None:
                invertedTree.left = self.invertTree(root.right)
            if root.left is not None:
                invertedTree.right = self.invertTree(root.left)
            return invertedTree
