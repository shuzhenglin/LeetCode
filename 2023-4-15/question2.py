class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m, n = min(len(s) for s in strs), len(strs) # 最长公共前缀受限于最短字符串，j只需满足最短字符串长度
        for j in range(m): # 循环体内先固定住j，字符串逐个字符进行比较
            for i in range(n):
                if strs[i][j] != strs[0][j]:
                    return strs[0][:j]
        return strs[0][:m]