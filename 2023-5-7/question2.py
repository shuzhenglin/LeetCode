class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(num, temp):
            if not num:
                res.append(temp) 
                return
            for i in range(len(num)):
                backtrack(num[:i] + num[i + 1:], temp + [num[i]])
        backtrack(nums, [])
        return res