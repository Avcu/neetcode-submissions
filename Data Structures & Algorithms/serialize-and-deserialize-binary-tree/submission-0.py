# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []

        def dfs(node):
            if not node:
                arr.append("None")
            else:
                arr.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ",".join(arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        self.idx = 0

        def dfs():
            if arr[self.idx] == "None":
                self.idx += 1
                return None
            else:
                currVal = int(arr[self.idx])
                self.idx += 1
                newNode = TreeNode(val=currVal)
                newNode.left = dfs()
                newNode.right = dfs()
                return newNode

        return dfs()
