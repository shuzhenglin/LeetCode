class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums) # 去重
        for i in range(1, len(nums)+1):
            if i not in nums_set:
                return i
        return len(nums)+1