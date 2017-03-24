class Solution(object):
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		def is_queue(depth, j):
			for i in range(depth):
				if border[i] == j or abs(depth - i) == abs(border[i] - j):
					return False
			return True

		def dfs(depth, row):
			if depth == n:
				ans.append(row)
				return
			for i in range(n):
				if is_queue(depth, i) is True:
					border[depth] = i
					dfs(depth + 1, row + ['.' * i + 'Q' + '.' * (n - i - 1)])
		border = [-1 for i in range(n)]
		ans = []
		dfs(0, [])
		return ans

if __name__ == '__main__':
	s = Solution()
	print s.solveNQueens(4)