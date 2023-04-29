class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        index = -1
        if not nums:
            return [-1, -1]
        while left <= right: # left=right的情况也要进去循环，因为必须要更新index
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left = index
        right = index # 将找到的目标值的索引赋值给左右两个指针
        while left >= 0 and nums[left] == target: # 两个指针分别向右和向左遍历，知道下标对应的元素不等于目标值
            left -= 1
        while right < n and nums[right] == target:
            right += 1
        return [left + 1, right - 1] if index != -1 else [-1, -1] # 列表中有目标值则返回目标值在数组中的开始位置和结束位置，没有则返回[-1, -1]