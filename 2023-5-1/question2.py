class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        new_list = []
        # 判断每一行是否重复
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    new_list.append(board[i][j])
            if len(new_list) != len(set(new_list)): # 判断方法为：将数字加入列表，set函数会创建一个不重复的元素集，和原始的列表进行长度的比较，如果不同则代表有重复元素
                return False
            new_list = []
        # 判断每一列是否重复
        for j in range(9):
            for i in range(9):
                if board[i][j] != '.':
                    new_list.append(board[i][j]) 
            if len(new_list) != len(set(new_list)):
                return False
            new_list = []
        # 判断每个9宫格是否重复
        m, n = 3, 3
        while m <= 9 and n <= 9:
            for i in range(m - 3, m):
                for j in range(n - 3 ,n):
                    if board[i][j] != '.':
                        new_list.append(board[i][j])
            if len(new_list) != len(set(new_list)):
                return False
            m += 3 # 横向移动9宫格
            if m > 9: # 纵向移动9宫格
                n += 3
                m = 3 # 复位横向9宫格位置
            new_list = []
        return True