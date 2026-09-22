class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        resList = []
        cur = []
        arr = range(1, n+1, 1)

        def dfs(i, j):
            if i >= n:
                if j == k:
                    resList.append(cur.copy())
                return
                
            # take 
            cur.append(arr[i])
            dfs(i+1, j+1)
            cur.pop()

            # skip
            dfs(i+1, j)
        
        dfs(0, 0)
        return resList