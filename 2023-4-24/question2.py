class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for k in range(n - m + 1):
            if haystack[k] == needle[0]:
                i = k
                j = 0
                while j < m and i < n and haystack[i] == needle[j]: # 需要先判断i，j是否还在字符串范围内，不然会out of range
                    i += 1
                    j += 1
                if j == m: # 如果字符串完全匹配，返回首次匹配的字符
                    return k
        return -1