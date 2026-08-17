# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                # root.val == key
                if root.left is None and root.right is None:
                    return None
                elif root.left is not None and root.right is None:
                    return root.left
                elif root.left is None and root.right is not None:
                    return root.right
                else:
                    curr = root.left
                    while curr.right is not None:
                        curr = curr.right

                    root.val = curr.val

                    root.left = self.deleteNode(root.left, root.val)

        return root
                    