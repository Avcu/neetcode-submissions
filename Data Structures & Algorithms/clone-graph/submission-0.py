"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneDict = {}

        def dfs(node):
            if node is None:
                return None
            elif node in cloneDict:
                return cloneDict[node]
            else:
                newNode = Node(val=node.val, neighbors=[])
                cloneDict[node] = newNode
                for neighbor in node.neighbors:
                    newNode.neighbors.append(dfs(neighbor))
                return newNode

        return dfs(node)