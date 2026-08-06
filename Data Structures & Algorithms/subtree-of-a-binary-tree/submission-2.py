# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        
        
    def isSameTree(self, root, anotherRoot) -> bool:
            if (root and not anotherRoot) or (not root and anotherRoot):
                return False
            elif not root and not anotherRoot:
                return True
            else:
                return root.val == anotherRoot.val and self.isSameTree(root.right, anotherRoot.right) and self.isSameTree(root.left, anotherRoot.left)
        