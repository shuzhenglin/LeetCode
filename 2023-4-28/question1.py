class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        tag = True # 设置标记，如果不存在下一个更大的排列，则变为最小排列
        while i > 0:
            if nums[i - 1] < nums[i]: # 从列表末端往前遍历，找到第一个不满足降序排列的元素i-1
                index = i
                while index < n and nums[i - 1] < nums[index]: # 找到大于元素i-1且与其最接近的元素，由于元素i之后都是降序，故最后一个大于i-1的必然是最接近i-1的
                    index += 1
                temp = nums[i - 1]
                nums[i - 1] = nums[index - 1]
                nums[index - 1] = temp # 交换操作
                nums[i:] = sorted(nums[i:]) # 对i后的元素进行重新排序
                tag = False # 这种情况属于存在下一个更大的排列
                break
            i -= 1
        if tag:
            nums.sort()