#!/usr/bin/env python
class Solution(object):
	def integerBreak(self, n):
		if n < 4:
			return n - 1
		res = 1
		while n - 3 >= 0:
			res *= 3
			n -= 3
		if n % 3 == 1:
			res /= 3
			res *= 4
		if n % 3 == 2:
			res *= 2
		return res

if __name__ == '__main__':
	s = Solution()
	n = 10
	print s.integerBreak(n)
