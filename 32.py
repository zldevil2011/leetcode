class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		stack = []
		max_len = 0
		last = -1
		for i in range(len(s)):
			if s[i] == '(':
				stack.append(i)
			else:
				if not stack:
					last = i
				else:
					stack.pop()
					if not stack:
						max_len = max(max_len, i - last)
					else:
						max_len = max(max_len, i - stack[-1])
		return max_len

if __name__ == '__main__':
	s = Solution()
	print s.longestValidParentheses("(()")