class Solution(object):
	def myPow1(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		if n == 0:
			return 1
		elif n < 0:
			return 1.0/self.myPow(x, -n)
		if n % 2 == 1:
			return x * self.myPow(x*x, n/2)
		else:
			return self.myPow(x*x, n/2)
	def myPow(self, x, n):
		if n < 0:
			fg = 1
			n = -n
		else:
			fg = 0
		res = 1
		while n > 0:
			if n % 2 == 1:
				res = res * x
			x = x*x
			n /= 2
		if fg == 0:
			return res
		else:
			return 1.0/res