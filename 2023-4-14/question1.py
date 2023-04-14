class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height) - 1
        i = 0 # 取i,j分别位于列表两端
        max_volume = 0 # 保存最大容积
        while i < j:
            # 水深由短板决定，向内移动短板可能增加容积，向内移动长板容积必然减小
            if height[i] < height[j]:
                volume = height[i]*(j - i)
                i += 1
            else:
                volume = height[j]*(j - i)
                j -= 1
            max_volume = max(volume, max_volume)
        return max_volume