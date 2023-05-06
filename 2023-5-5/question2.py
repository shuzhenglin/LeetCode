class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        h1, h2 = 0, 0
        volume = 0 # 存放雨水体积
        for i in range(n):
            h1 = max(h1, height[i])
            h2 = max(h2, height[-i-1])
            volume += h1 + h2 - height[i] # 这样雨水的体积多了一个以最高柱子为高，以列表长度为底的矩形，因为h1,h2在遍历到最高的柱子后便不再更新了，两边组合正好是这个矩形
        volume -= h1 * n
        return volume