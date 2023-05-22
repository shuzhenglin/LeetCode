class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        agg_list = []
        def backtrack(i, agg, elem): # i, agg, elem分别表示列表下标，组合总和，组合列表
            if agg == target: # 
                agg_list.append(elem)
                return
            for j in range(i, n):
                if agg + candidates[j] > target:
                    break
                backtrack(j, agg + candidates[j], elem + [candidates[j]])
        backtrack(0, 0, [])
        return agg_list