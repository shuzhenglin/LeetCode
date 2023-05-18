class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_len, str_len = len(words), len(s)
        key_len = len(words[0]) # 依次取列表，字符串，列表内字符串元素长度
        agg = key_len * words_len # 计算出连接的子字符串长度
        k = 0
        res = [] # res为最终返回的输出    
        while str_len - k >= agg: # 余下的字符数量不满足连接的子字符串长度，退出循环
            i = 0
            table = [] # 引入列表，存放切片
            ans = s[k: k + agg] # 设置滑动窗口，每次在字符串s取下长度为agg的字符串
            for j in range(words_len):
                table.append(ans[j * key_len: (j + 1) * key_len]) #对ans字符串进行切片
            while i < words_len:
                if words[i] in table: # 在列表table中寻找words中的字符串
                    table.remove(words[i]) # 移除掉已经完成匹配的字符串
                    i += 1
                else:
                    break
            if i == words_len: # words中的所有字符串完成匹配，将开始索引加入列表res
                res.append(k)
            k += 1
        return res