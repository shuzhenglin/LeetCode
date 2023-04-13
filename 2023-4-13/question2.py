class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1)  for _ in range(n + 1)]
        dp[0][0] = True # 匹配0个字符时为True
        for j in range(1, m+1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2] # 匹配0个字符串，类似'*'的字符为一组，复制0次，继承2个字符以前的状态
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.') 
                    # 扫描到的字符不为'*'的情况，判断s和p字符串在i，j位置是否相同，或p在j位置是否为'.'，并和上一个状态做与运算
                else:
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                    # 扫描到的字符是'*'的情况分为两种，
                    # ①以'a*'为单位复制0次，直接继承2个字符前的状态即可 
                    # ②以'a*'为单位复制1次及以上，由于p可以用较短的字符长度匹配s的较长长度，
                    # 可以继承s在一个字符之前和p当前字符的匹配状态，并要求s第i个字符和p的第j-1个字符相同或者p的第j-1个字符为'.'
        return dp[n][m]