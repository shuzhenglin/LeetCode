class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        if not nums:
            return -1
        while left <= right:
            # 本质还是二分查找，不过是需要分两种情况进行
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # 由于列表有两段升序排列，nums[left]<=nums[mid]代表mid左边仍然有序，再看target处于哪段序列
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1