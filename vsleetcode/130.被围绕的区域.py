#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(board):
            for j in range(board):
                if board[i][j]=="O":
                    boundary=[board[i-1][j],board[i+1][j],board[i][j-1],board[i][j+1]]
                    if O in boundary:
                        board[i][j]=X
        

# @lc code=end

