class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = set()# 引入集合，方便移除重复元素
        max_len = 0
        left = 0 # 表示子串左端
        for right, ch in enumerate(s): # 拆分成hash表，right表示子串最右端
            while ch in table:
                table.remove(s[left]) # 注意只能是字串
                left += 1 # left必须从当前子串集合的最左边移动
            table.add(ch) # 子串里没有重复，继续向集合里添加字符
            max_len = max(max_len, right - left + 1)# 保留最长的子串长度
        return max_len