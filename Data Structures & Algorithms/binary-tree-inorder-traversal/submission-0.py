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
        ## if there is no more child, add the value to the list
        if (root.left is None) and (root.right is None):
            outputList.append(root.val)
        ## if there is a left child but no right child
        elif (root.left is not None) and (root.right is None):
            outputList.extend(self.inorderTraversal(root.left))
            outputList.append(root.val)
        ## if there is a right child but no left child
        elif (root.left is None) and (root.right is not None):
            outputList.append(root.val)
            outputList.extend(self.inorderTraversal(root.right))
        else:
            outputList.extend(self.inorderTraversal(root.left))
            outputList.append(root.val)
            outputList.extend(self.inorderTraversal(root.right))
        return outputList
        