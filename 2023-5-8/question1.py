class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(num, temp):
            if not num and temp not in res:
                res.append(temp)
                return
            for i in range(len(num)):
                backtrack(num[:i] + num[i+1:], temp + [num[i]])
        backtrack(nums, [])
        return res