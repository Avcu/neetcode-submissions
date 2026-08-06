# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def existInTree(root: TreeNode, p: TreeNode):
            if not root or not p:
                return False
            if p == root:
                return True
            else:
                return existInTree(root.left, p) or existInTree(root.right, p)
        
        curr = root
        while curr:
            if existInTree(curr.left, p) and existInTree(curr.left, q):
                curr = curr.left
            elif existInTree(curr.right, p) and existInTree(curr.right, q):
                curr = curr.right
            else:
                return curr