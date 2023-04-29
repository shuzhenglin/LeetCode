class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        res = 0
        for i in range(n):
            # 需要入栈的几种情况： 
            # I.当前栈为空，当前字符s[i]无法和前面的字符匹配
            # II.s[i]是左括号'('
            # III.栈顶元素是右括号')'，无论当前字符s[i]是什么，都无法和栈顶元素构成一对括号，其实也就是栈顶元素必须为'('，当前字符s[i]必须为')'，这样才能构成一对括号
            if not stack or s[i] == '(' or s[stack[-1]] == ')': 
                stack.append(i)
            else: # 可以构成有效字符的索引出栈
                stack.pop()
                res = max(res, i - (stack[-1] if stack else -1)) # 用当前索引减去当前栈顶的索引即暂时无法构成有效括号的索引，如果当前栈为空，则代表有效长度即为当前字符串长
        return res