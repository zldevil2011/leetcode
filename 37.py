class Solution(object):
	# def solveSudoku(self, board):
	# 	m = len(board)
	# 	n = len(board) if m else 0
	# 	seen, points =set(), []
	# 	for i in range(m):
	# 		for j in range(n):
	# 			if board[i][j] == '.':
	# 				points.append((i, j))
	# 			else:
	# 				seen.update([str(i) + 'r' + board[i][j], str(j) + 'c' + board[i][j], str(i/3) + str(j/3) + board[i][j]])
	# 	def dfs(points, i, board, v):
	# 		if i == len(points): return True
	# 		x, y = points[i]
	# 		for j in range(1, 10):
	# 			tmp = set([str(x) + 'r' + str(j), str(y)+ 'c'+ str(j), str(x/3) + str(y/3) + str(j)])
	# 			if not tmp&v:
	# 				board[x][y] = str(j)
	# 				if dfs(points, i + 1, board, v | tmp ): return True
	# 				board[x][y] = '.'
	# 		return False
	# 	dfs(points, 0, board, seen)
	def new_solve(self, board):
		for i in range(9):
			for j in range(9):
				if board[i][j] == '.':
					for k in range(1,10):
						board[i][j] = str(k)
						if self.valid_test(board, i, j) and self.new_solve(board):
							return True
						board[i][j] = '.'
					return False
		return True

	def valid_test(self, board, row, col):
		for i in range(9):
			if i != col and board[row][col] == board[row][i]:
				return False
		for i in range(9):
			if i != row and board[row][col] == board[i][col]:
				return False
		b_row = 3 * (row / 3)
		b_col = 3 * (col / 3)
		for i in range(b_row, b_row + 3):
			for j in range(b_col, b_col + 3):
				if i != row and j != col and board[i][j] == board[row][col]:
					return False
		return True
# 	def dfs(self, board):
# 		for row in range(0, 9):
# 			for col in range(0, 9):
# 				if board[row][col] == '.':
# 					for char in '123456789':
# 						board[row][col] = char
# 						if self.isValidSudoku(board) and self.dfs(board):
# 							return False
# 						board[row][col] = '.'
# 					return False
# 		return True
#
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		new_board = []
		for s in board:
			new_board.append(list(s))
		res = self.new_solve(new_board)
		# board = []
		for idx, s in enumerate(new_board):
			t = "".join(s)
			board[idx] = t
		# print board
#
# 	def solve(self, board, position):
# 		if position == 81:
# 			return True
# 		row = position / 9
# 		col = position % 9
# 		if board[row][col] == '.':
# 			for i in range(1, 10):
# 				board[row][col] = str(i)
# 				if self.isValidSudoku(board) is True:
# 					if self.solve(board, position + 1):
# 						return True
# 				board[row][col] = '.'
# 		else:
# 			if self.solve(board, position + 1) is True:
# 				return True
# 		return False
#
# 	def isValidSudoku(self, board):
# 		"""
# 		:type board: List[List[str]]
# 		:rtype: bool
# 		"""
# 		if len(board) == 0:
# 			return False
# 		l = len(board)
# 		for i in range(l):
# 			cnt = [0 for j in range(0, 9)]
# 			for k in range(l):
# 				if board[i][k] != '.':
# 					num = int(board[i][k]) - 1
# 					if cnt[num] > 0:
# 						return False
# 					else:
# 						cnt[num] += 1
# 		for i in range(l):
# 			cnt = [0 for j in range(0, 9)]
# 			for k in range(l):
# 				if board[k][i] != '.':
# 					num = int(board[k][i]) - 1
# 					if cnt[num] > 0:
# 						return False
# 					else:
# 						cnt[num] += 1
# 		for i in range(0, 9, 3):
# 			for j in range(0, 9, 3):
# 				cnt = [0 for ii in range(0, 9)]
# 				for row in range(0, 3):
# 					for col in range(0,3):
# 						if board[i + row][j + col] != '.':
# 							num = int(board[i + row][j + col]) - 1
# 							if cnt[num] > 0:
# 								return False
# 							else:
# 								cnt[num] += 1
# 		return True
#
if __name__ == '__main__':
	board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
	s = Solution()
	s.solveSudoku(board)
	print board