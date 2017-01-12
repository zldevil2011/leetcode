class Solution(object):
	def longestPalindrome(self, s):
		if len(s) <= 1:
			return s
		max_l = 0
		res = ""
		l = len(s)
		for i in range(l):
			ll = i
			rr = i
			tmp = self.getlr(s, ll, rr)
			if len(tmp) > max_l:
				max_l = len(tmp)
				res = tmp
			if i != (len(s) - 1):
				ll = i
				rr = i + 1
				tmp = self.getlr(s, ll, rr)
				if len(tmp) > max_l:
					max_l = len(tmp)
					res = tmp
		return res

	def getlr(self, s, l, r):
		while l>=0 and r < len(s) and s[l] == s[r]:
			l -= 1
			r += 1
		return s[l+1:r]

	def longestPalindrome1(self, s):
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
	print s.longestPalindrome("babad")