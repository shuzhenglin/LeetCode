class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = numRows*2 - 2 # 找到周期数量n，字符串以n的数量为周期进行N子排列
        res = [''] * numRows # 设置一个字符串集合，字符串的下标相当于矩阵的行数
        for i, ch in enumerate(s):
            idx = i % n
            res[min(idx, n - idx)] += ch # 将字符串按照行数加入新的字符串集合
        return ''.join(res) # 新的字符串按行拼接