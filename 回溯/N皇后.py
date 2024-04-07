"""
题目：
    n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
    每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
"""


class Solution:
    def solveNQueens(self, n):
        result = []
        row = 0
        chessboard = ['.' * n for _ in range(n)]
        self.backtracing(n, chessboard, row, result)
        return [[''.join(s) for s in solution] for solution in result]

    def backtracing(self, n, chessboard, row, result):
        if row == n:
            result.append(chessboard[:])
            return
        for col in range(n):
            if self.isValid(chessboard, row, col):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                self.backtracing(n, chessboard, row+1, result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col + 1:]

    def isValid(self, chessboard, row, col):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row-1, col+1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True


n = 4
g = Solution()
print("""正确答案：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]""")
result = g.solveNQueens(n)
print(result)