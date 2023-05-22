class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n > 1: # 递归
            s = self.countAndSay(n - 1)
            t = ''
            i, j = 0, len(s)
            count = 1 # 记录相同数字个数
            while i < j:
                if i + 1 < j and s[i] == s[i + 1]:
                    count += 1
                else:
                    t += str(count) + s[i] # 叠加字符串
                    count = 1
                i += 1
            return t