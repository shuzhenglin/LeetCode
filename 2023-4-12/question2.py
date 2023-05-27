class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''
        tag = 0
        num = 0
        s = s.lstrip() # 去掉前导空格
        if len(s) == 0:
            return 0
        if s[0] == '-': # 检查下一个字符是‘＋’是‘-’，打好标记
            s = s[1:]
            tag = 1
        elif s[0] == '+': 
            s = s[1:]
            tag = 0
        for j in range(len(s)):# 将数字字符存入res
            if s[j].isdigit():
                res += s[j]
            else: # 继正负号后的字符不是数字将直接弹出循环，最后结果为0
                break
        for ch in res:
            num = num*10 + int(ch)
        if tag == 1:
            num = -num
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        return num