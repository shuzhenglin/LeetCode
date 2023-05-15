class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        dev = 10**5 # 根据题目要求，3数之和范围-3000~3000，和target的最大距离为13000，故取dev = 10^5
        res = 0
        for i in range(n):
            left = i + 1
            right = n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                agg = nums[i] + nums[left] + nums[right]
                cur = abs(agg - target) # 计算当前3数之和与目标的距离
                if agg == target:
                    return target
                elif agg < target:
                    left += 1
                else:
                    right -= 1
                if dev > cur: # 更新最小距离，保存当前的3数之和
                    dev = cur
                    res = agg
        return res