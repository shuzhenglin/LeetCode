class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            keys = ''.join(sorted(s)) # 对数组中的字符串排序，使字母异位词拥有相同的关键字
            if keys not in dic: # 如果哈希表中没有此关键字，则创建一个新的关键字，将字符串列表作values
                dic[keys] = [s]
            else: # 如果已有关键字，则加入相应的关键字内
                dic[keys].append(s)
        return list(dic.values())