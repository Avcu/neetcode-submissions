# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        myDeque = deque()

        myDeque.append([root, 1])
        maxLevel = 1

        while myDeque:
            [poppedNode, level] = myDeque.pop()
            if poppedNode is not None:
                maxLevel = max(maxLevel, level)
                myDeque.append([poppedNode.right, level+1])
                myDeque.append([poppedNode.left, level+1])
        return maxLevel
