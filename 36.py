class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		if len(board) == 0:
			return False
		l = len(board)
		for i in range(l):
			cnt = [0 for j in range(0, 9)]
			for k in range(l):
				if board[i][k] != '.':
					num = int(board[i][k]) - 1
					if cnt[num] > 0:
						return False
					else:
						cnt[num] += 1
		for i in range(l):
			cnt = [0 for j in range(0, 9)]
			for k in range(l):
				if board[k][i] != '.':
					num = int(board[k][i]) - 1
					if cnt[num] > 0:
						return False
					else:
						cnt[num] += 1
		for i in range(0, 9, 3):
			for j in range(0, 9, 3):
				cnt = [0 for ii in range(0, 9)]
				for row in range(0, 3):
					for col in range(0,3):
						if board[i + row][j + col] != '.':
							num = int(board[i + row][j + col]) - 1
							if cnt[num] > 0:
								return False
							else:
								cnt[num] += 1
		return True
