class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges)+1)]     # n is included, so n+1

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(ite, startNode, endNode):
            if ite == endNode:
                return True
            else:
                seen.add(ite)
                resBool = False
                for neighbor in adj[ite]:
                    if neighbor in seen or (ite == startNode and neighbor == endNode):
                        continue
                    else:
                        stack.append(neighbor)
                        resBool = resBool or dfs(neighbor, startNode, endNode)
                return resBool


        for idx in range(len(edges)-1,-1,-1):
            seen = set()
            stack = []
            currEdge = edges[idx]
            
            stack.append(currEdge[0])
            if dfs(currEdge[0], currEdge[0], currEdge[1]):
                return currEdge