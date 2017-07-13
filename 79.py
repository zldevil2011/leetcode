class Solution(object):
	def __init__(self):
		self.x_dir = [0,1,0,-1]
		self.y_dir = [1,0,-1,0]

	def exist(self, board, word):
		'''
		:param board: List[List[str]]
		:param word: str
		:return: bool
		'''
		n = len(board)
		m = len(board[0])
		for i in range(n):
			for j in range(m):
				c = board[i][j]
				if c == word[0]:
					visied = [[0 for ii in range(m)] for jj in range(n)]
					visied[i][j] = 1
					if self.dfs(i, j, 1, n, m, board,word,visied) is True:
						return True
		return False

	def judge(self,x,y,n,m):
		if x < 0 or y < 0 or x >= n or y >= m:
			return False
		return True

	def dfs(self, x, y, pos, n, m, board, word, visited):
		if pos == len(word):
			return True
		for ix in range(4):
			xx = self.x_dir[ix]
			yy = self.y_dir[ix]
			nx = x + xx
			ny = y + yy
			if self.judge(nx,ny,n,m) is True and board[nx][ny] == word[pos] and visited[nx][ny] == 0:
				visited[nx][ny] = 1
				if self.dfs(nx,ny,pos+1,n,m,board,word,visited) is True:
					return True
				visited[nx][ny] = 0
		return False



if __name__ == '__main__':
	s = Solution()
	board = [
		['A','B','C','E'],
		['S','F','C','S'],
		['A','D','E','E']
	]
	word = "ABCB"
	print(s.exist(board, word))