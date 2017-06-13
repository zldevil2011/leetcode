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

# O(n) Algorithm
# http: // articles.leetcode.com / longest - palindromic - substring - part - ii


# ll = len(s)
	# res = self.LR(s, 0, ll - 1, 0, "", 0, "")
	# return res
	# def LR(self, s, l, r, cur_ll, cur_str, max_ll, max_str):
	# 	while l <= r:
	# 		if s[l] == s[r] and l != r:
	# 			L = len(cur_str)
	# 			LL = 0
	# 			RR = L - 1
	# 			tmp = ""
	# 			while LL < L / 2:
	# 				tmp += cur_str[LL]
	# 				LL += 1
	# 			tmp += s[l]
	# 			while RR >= L / 2:
	# 				tmp += cur_str[RR]
	# 				RR -= 1
	# 			tmp += s[r]
	# 			cur_str = tmp
	# 			l += 1
	# 			r += 1
	# 			cur_ll += 2
	# 			return self.LR(s, l, r, cur_ll, cur_str, max_ll, max_str)
	# 		elif s[l] == s[r] and l == r:
	# 			L = len(cur_str)
	# 			LL = 0
	# 			RR = L - 1
	# 			tmp = ""
	# 			while LL < L / 2:
	# 				tmp += cur_str[LL]
	# 				LL += 1
	# 			tmp += s[l]
	# 			while RR >= L / 2:
	# 				tmp += cur_str[RR]
	# 				RR -= 1
	# 			cur_str = tmp
	# 			if len(cur_str) > len(max_str):
	# 				max_str = cur_str[:]
	# 				return max_str
	# 			else:
	# 				return max_str
	# 		else:
	# 			L_cur_str = cur_str[:]
	# 			R_cur_str = cur_str[:]
	# 			L_max_str = max_str[:]
	# 			R_max_str = max_str[:]
	# 			L_new_l = l + 1
	# 			L_new_r = r
	# 			R_new_l = l
	# 			R_new_r = r - 1
	# 			l_str = self.LR(s, L_new_l, L_new_r, cur_ll, L_cur_str, max_ll, L_max_str)
	# 			r_str = self.LR(s, R_new_l, R_new_r, cur_ll, R_cur_str, max_ll, R_max_str)
	# 			return l_str if len(l_str) > len(r_str) else r_str
	# 	return max_str