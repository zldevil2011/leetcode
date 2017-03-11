class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		n = len(s)
		start = 0
		end = 0
		max_len = 0
		tmp_len = 0
		red = []
		while end < n:
			try:
				pos = red.index(s[end])
				while s[start] != s[end]:
					red.remove(s[start])
					start += 1
				start += 1
				end += 1
			except:
				red.append(s[end])
				end += 1
			tmp_len = end - start
			max_len = max(max_len, tmp_len)
		return max_len

if __name__ == '__main__':
	s = Solution()
	print s.lengthOfLongestSubstring("abcabcbb")