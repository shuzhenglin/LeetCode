class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        # 特殊情况，当n<4时，返回空列表
        #当n=4时，计算列表数字总和，进行判断
        if n < 4:
            return []
        elif n == 4:
            return [nums] if sum(nums) == target else []
        # i,j为循环主体，保持i<j
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                L = j + 1
                R = n - 1
                while L < R:
                    agg = nums[i] + nums[j] + nums[L] + nums[R]
                    if agg == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        L += 1
                        R -= 1
                    elif agg < target:
                        L += 1
                    else:
                        R -= 1
        return res