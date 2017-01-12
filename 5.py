class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		# dramatic plan
		if len(s) <= 1:
			return s
		l = len(s)
		dp = [[0 for i in range(l)] for i in range(l)]
		for i in range(l):
			dp[i][i] = 1
		max_l = 1
		res = s[0]
		for i in range(l):
			for j in range(i):
				if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1] == 1):
					dp[j][i] = 1
				if dp[j][i] == 1:
					if i - j + 1 > max_l:
						max_l = i - j + 1
						res = s[j:i+1]
		return res

if __name__ == '__main__':
	s = Solution()
	print s.longestPalindrome("abcda")