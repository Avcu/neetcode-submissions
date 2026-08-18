class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        resSet = set()
        candidates.sort()
        
        def dfs(idx, arr, total):
            if total == target:
                resSet.add(tuple(arr))
                return
            if idx == len(candidates) or total+candidates[idx] > target:
                return

            arr.append(candidates[idx])
            dfs(idx+1, arr, total+candidates[idx])
            arr.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1, arr, total)
                

        dfs(0, [], 0)
        return [list(x) for x in resSet]