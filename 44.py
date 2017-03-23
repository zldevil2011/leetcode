class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		i = 0
		j = 0
		sstar = 0
		star = -1
		while i < len(s):
			if j < len(p) and (s[i] == p[j] or p[j] == '?'):
				i += 1
				j += 1
			elif j < len(p) and p[j] == '*':
				star = j
				j += 1
				sstar = i
			elif star != -1:
				j = star + 1
				sstar += 1
				i = sstar
			else:
				return False
		while j < len(p) and p[j] == '*':
			j += 1
		if j == len(p):
			return True
		return False
