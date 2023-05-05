class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        agg_list = []
        def backtrack(i, agg, elem):
            if agg == target:
                agg_list.append(elem)
                return
            for j in range(i, n):
                if agg + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                backtrack(j + 1, agg + candidates[j], elem + [candidates[j]])
        backtrack(0, 0, [])
        return agg_list