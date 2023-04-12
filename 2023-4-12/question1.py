class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-': # x为负数，则将x从第1位至倒数第一位逆置
            res = int(s[: 0: -1])
            res = -res # 添加负号
        else: # x为正数，将x从第0位至倒数第一位逆置
            res = int(s[::-1])
        if -2**31 <= res <= 2**31 - 1:
            return res
        else:
            return 0