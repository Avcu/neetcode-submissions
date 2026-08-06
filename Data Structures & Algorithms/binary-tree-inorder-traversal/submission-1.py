# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        outputList = []
        if root is None:
            return outputList

        # if there is a left child, add it
        if root.left is not None:
            outputList.extend(self.inorderTraversal(root.left))
        outputList.append(root.val)
        # if there is a right child, add it
        if root.right is not None:
            outputList.extend(self.inorderTraversal(root.right))
            
        return outputList
        