# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levelList = []
        rightSideView = []

        def dfs(root, level):
            if not root:
                return None
            if len(levelList) == level:
                levelList.append([])
            
            levelList[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root, 0)
        for level in levelList:
            rightSideView.append(level[-1])

        return rightSideView
