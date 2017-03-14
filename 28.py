class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		h_len = len(haystack)
		n_len = len(needle)
		if n_len == 0:
			return 0
		next = self.get_next(needle)
		print(next)
		i = 0
		j = 0
		while i < h_len and j < n_len:
			if j == -1 or haystack[i] == needle[j]:
				i += 1
				j += 1
			else:
				print i, j
				j = next[j]
		if j == n_len:
			return i - n_len
		else:
			return -1

	def get_next(self, needle):
		n_len = len(needle)
		next = [0 for i in range(n_len)]
		j = -1
		i = 0
		next[i] = -1
		while i < n_len - 1:
			if j == -1 or needle[i] == needle[j]:
				j += 1
				i += 1
				next[i] = j
			else:
				j = next[j]
		return next

if __name__ == '__main__':
	s = Solution()
	print s.strStr("aaacaaabaabab", "aaabaabab")
	print s.strStr("qqqqqqqqqqqqqqqqqqqqq", "aabaababb")
	print s.strStr("qqqqqqqqqqqqqqqqqqqqq", "abcaacbbcbadaabcacbd")
