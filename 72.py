class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		m,n = len(word1), len(word2)
		ans = [[0 for i in range(n + 1)] for j in range(m+1)]
		for i in range(m+1):
			ans[i][0] = i
		for i in range(n+1):
			ans[0][i] = i
		for i in range(1, m + 1):
			for j in range(1, n+1):
				if word1[i-1] == word2[j-1]:
					ans[i][j] = ans[i-1][j-1]
				else:
					ans[i][j] = min(ans[i-1][j-1], ans[i-1][j], ans[i][j-1]) + 1
		return ans[m][n]




if __name__ == '__main__':
	word1 = "ab"
	word2 = "bc"
	s = Solution()
	print s.minDistance(word1, word2)