class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 初始化dp
        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, m + 1): # 要匹配空字符串，需要遍历到'*'
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        # 状态转移
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?': # 普通情况
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == '*':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] # 两种情况，'*'代表空字符/代表任何字符序列
        return dp[n][m]