class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        resSet = set()
        subset = []
        candidates.sort()
        
        def dfs(idx, total):
            if total == target:
                resSet.add(tuple(subset))
                return
            if idx == len(candidates) or total+candidates[idx] > target:
                return

            subset.append(candidates[idx])
            dfs(idx+1, total+candidates[idx])
            subset.pop()

            # skip the duplicate elements
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1, total)
                

        dfs(0, 0)
        return [list(x) for x in resSet]