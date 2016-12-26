class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        height = len(board)
        if height == 0:
            return 0
        width = len(board[0])
        ans = 0
        for i in range(height):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    pass
                elif i > 0 and board[i-1][j] == 'X':
                    pass
                elif j > 0 and board[i][j-1] == 'X':
                    pass
                else:
                    ans += 1
        return ans
        
if __name__ == '__main__':
    test = [['X','.', '.', 'X'], ['.','.','.','X'],['.','.','.','X']]
    s = Solution()
    print(s.countBattleships(test))