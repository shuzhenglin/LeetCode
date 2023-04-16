class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort() # 对列表顺序排序
        for i in range(n):
            left = i + 1
            right = n - 1 # 引入指针left,right分别指向以i为边界的首尾两个元素
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: # 当边界i和上一个边界相等时，不用重复讨论
                continue
            while left < right:
                agg = nums[i] + nums[left] + nums[right]
                if agg == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    # 和为0时，移动指针如果下个值相同，不再重复考虑
                elif agg > 0:
                    right -= 1
                else:
                    left += 1
        return res