class Solution(object):
	def isPalindrome(self, x):
		if x < 0:
			return False
		x = str(x)
		if len(x) == 1:
			return True
		start = 0
		end = len(x) - 1
		while start <= end:
			if x[start] != x[end]:
				return False
			start += 1
			end -= 1
		return True

	def isPalindrome1(self, x):
		if x < 0:
			return False
		d_num = 1
		while (x / d_num) >= 10:
			d_num *= 10
		while x != 0:
			l = x / d_num
			r = x % 10
			if l != r:
				return False
			x = (x % d_num) / 10
			d_num /= 100
		return True

if __name__ == '__main__':
	s = Solution()
	print s.isPalindrome1(12345)
	print s.isPalindrome1(12321)