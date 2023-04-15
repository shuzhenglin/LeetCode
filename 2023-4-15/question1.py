class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        n = len(s)
        ch = ''
        res, i = 0, 0
        while i < n:
            ch = s[i:i+2] # 每次截取连续的两个字符在hash表中进行查找
            if ch in hash_map: # 如果有value，则加上对应的value，下标加2
                res += hash_map[ch]
                i += 2
            else: # 如果在hash表中没找到相应的key，则用单个字符进行查找，下标加1
                res += hash_map[s[i]]
                i += 1
        return res