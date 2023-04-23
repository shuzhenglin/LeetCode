class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        for i in range(1, n):
            if nums[j] != nums[i]:
                j += 1 # 先留出空位，再存放元素
                nums[j] = nums[i]
        return j + 1