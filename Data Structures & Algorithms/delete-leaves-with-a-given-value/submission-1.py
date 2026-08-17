# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def isLeaf(node):
            if node is None:
                return False
            else:
                return node.right is None and node.left is None

            
        def dfs(root, target):
            if root is None:
                return None

            root.left = dfs(root.left, target)
            root.right = dfs(root.right, target)

            if isLeaf(root) and root.val == target:
                return None
            return root

        return dfs(root, target)