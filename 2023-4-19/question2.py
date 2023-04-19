class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 深度优先遍历
        res = [] 
        def dfs(path, left, right):
            if left > n or right > left: # '('数量大于n时无效，'('数量小于n时，')'数量大于'('
                return
            if len(path) == 2 * n:
                res.append(path)
                return
            dfs(path + '(', left + 1, right) # 添加左子树'('
            dfs(path + ')', left, right + 1) # 添加右子树')'
        dfs('', 0, 0)
        return res