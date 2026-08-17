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

            dfs(root.left, target)
            dfs(root.right, target)

            if root.right is not None and isLeaf(root.right) and root.right.val == target:
                root.right = None
            if root.left is not None and isLeaf(root.left) and root.left.val == target:
                root.left = None

        dfs(root, target)
        
        if isLeaf(root) and root.val == target:
            return None
        else:
            return root