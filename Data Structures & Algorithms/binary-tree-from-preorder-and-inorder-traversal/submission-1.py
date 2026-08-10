# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookUp = {val: idx for idx, val in enumerate(inorder)}
        self.preIdx = 0

        def dfs(l, r) -> Optional[TreeNode]:
            if l > r:
                return None
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            mid = lookUp[rootVal]

            root = TreeNode(val=rootVal, left=dfs(l, mid-1), right=dfs(mid+1, r))
            return root

        return dfs(0, len(preorder)-1)
