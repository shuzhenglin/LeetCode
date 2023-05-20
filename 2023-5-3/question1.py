class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 生成无序但不重复的1-9元素，row,col,block分别存放给定board中每行，每列，每个九宫格未出现的1-9元素（行，列，九宫格列表数都为9）
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]
        table = [] # 存放待填入数字的位置(i， j)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[i // 3 * 3 + j // 3].remove(val)
                else:
                    table.append((i, j))
        
        def backtrack(count = 0):
            if count == len(table):
                return True
            i, j = table[count]
            b = i // 3 * 3 + j // 3
            for val in row[i] & col[j] & block[b]: # 取行，列，九宫格未出现的1-9元素的交集
                row[i].remove(val) # 更新解空间
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(count + 1):
                    return True
                row[i].add(val) # 回溯
                col[j].add(val)
                block[b].add(val)
            return
        backtrack()