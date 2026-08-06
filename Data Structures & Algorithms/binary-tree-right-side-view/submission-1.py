# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideView = []

        def dfs(root, level):
            if not root:
                return None
            if len(rightSideView) == level:
                rightSideView.append(root.val)
            dfs(root.right, level+1)
            dfs(root.left, level+1)

        dfs(root, 0)
        return rightSideView
