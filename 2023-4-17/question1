class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if not n:
            return []
        hash_map = {'2':['a', 'b', 'c'],
                    '3':['d', 'e', 'f'],
                    '4':['g', 'h', 'i'],
                    '5':['j', 'k', 'l'],
                    '6':['m', 'n', 'o'],
                    '7':['p', 'q', 'r', 's'],
                    '8':['t', 'u', 'v'],
                    '9':['w', 'x', 'y', 'z']}
        # 引入字典，每个key对应一组列表
        def backtrack(combination, nextdigit): # 申明一个函数进行递归
            if len(nextdigit) == 0:
                res.append(combination) # 将已经完成拼接的字符放入列表res
            else:
                for letter in hash_map[nextdigit[0]]: # 循环主体是字典中的value，即列表
                    backtrack(combination + letter, nextdigit[1:]) # 每次进入递归对数字字符串digits进行切片，让主体变为下一个列表
        res = [] # 创建列表存放组合字符
        backtrack('', digits) #第一次组合由空字符''+第一个列表字符
        return res