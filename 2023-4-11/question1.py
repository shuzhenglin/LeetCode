class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        left = 0
        max_len = 1
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)] #初始化dp
        for i in range(n):
            dp[i][i] = True

        for j in range(n): # 让dp矩阵从上到下，从左到右更新，否则状态转移方程会继承不正确的状态
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True # 长度小于等于3的子串满足s[i]==s[j]即是回文
                    else:
                        dp[i][j] = dp[i + 1][j - 1] # 状态转移
                if dp[i][j] and max_len < j - i + 1:
                    left = i
                    max_len = j - i + 1 # 保存并更新当前最长的回文子串长度
        return s[left:left + max_len]