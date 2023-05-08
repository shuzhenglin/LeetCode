class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        pre_dis = 0
        cur_dis = 0
        step = 0
        for i in range(n - 1): # 每次循环得到局部最优解
            cur_dis = max(nums[i] + i, cur_dis) # 随着下标的移动，每次更新最大的可跳覆盖范围
            if pre_dis == i: # 如果下标移动到上一个最大覆盖范围，将步数加一
                step += 1
                pre_dis = cur_dis
                if cur_dis >= n - 1: # 如果此时最大可跳覆盖范围超过数组长度，跳出循环
                    break
        return step