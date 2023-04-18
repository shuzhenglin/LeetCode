class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # 引入栈
        hash_map = {'(':')', '[':']', '{':'}'} # 引入hash表
        for ch in s:
            if ch in hash_map: # 如果字符对应key,则加入栈
                stack.append(ch)
            elif stack != []: # 如果字符对应value,弹出栈
                if hash_map[stack.pop()] != ch: # 如果弹出的key不能对应上自身的value，返回false
                    return False
            else:
                return False
        return True if stack == [] else False    